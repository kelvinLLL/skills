import json
import re
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List, Optional


REQUIRED_SECTIONS = [
    "一、基础设施与算力",
    "二、模型与研究",
    "三、研究与社区",
    "四、业界变动",
]

SECTION_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)
DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
SOURCE_DATE_URL_RE = re.compile(r"\[[^\]]*·\s*\d{4}-\d{2}-\d{2}\]\((https?://[^)\s]+)\)")
URL_RE = re.compile(r"\((https?://[^)\s]+)\)")
ENTRY_RE = re.compile(r"(?=^\*\*)", re.MULTILINE)
NO_UPDATE_RE = re.compile(r"今日暂无重大动态|今日无新动态")
MODEL_MODALITY_KEYWORDS = [
    "视频",
    "图像",
    "音频",
    "多模态",
    "ocr",
    "tts",
    "vision",
    "video",
    "image",
    "audio",
]


@dataclass
class ValidationWindow:
    target_date: date
    start_date: date
    end_date: date


def parse_iso_date(value: str) -> date:
    year, month, day = [int(part) for part in value.split("-")]
    return date(year, month, day)


def infer_target_date_from_text(text: str) -> Optional[str]:
    match = re.search(r"(\d{4})年(\d{1,2})月(\d{1,2})日", text)
    if not match:
        return None
    year, month, day = [int(part) for part in match.groups()]
    return f"{year:04d}-{month:02d}-{day:02d}"


def infer_target_date_from_path(report_path: Path) -> Optional[str]:
    match = DATE_RE.search(report_path.name)
    return match.group(0) if match else None


def build_window(target_date: str, window_days: int = 2) -> ValidationWindow:
    target = parse_iso_date(target_date)
    return ValidationWindow(
        target_date=target,
        start_date=target - timedelta(days=window_days),
        end_date=target + timedelta(days=window_days),
    )


def parse_sections(text: str) -> Dict[str, str]:
    matches = list(SECTION_RE.finditer(text))
    sections: Dict[str, str] = {}
    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[heading] = text[start:end].strip()
    return sections


def split_entry_blocks(section_body: str) -> List[str]:
    if not section_body.strip():
        return []
    blocks = [block.strip() for block in ENTRY_RE.split(section_body) if block.strip()]
    return [block for block in blocks if block.startswith("**")]


def make_check(name: str, passed: bool, detail: str, extra: Optional[dict] = None) -> dict:
    payload = {"name": name, "passed": passed, "detail": detail}
    if extra:
        payload.update(extra)
    return payload


def validate_report(report_path: Path, target_date: Optional[str] = None, window_days: int = 2) -> dict:
    report_path = Path(report_path)
    text = report_path.read_text(encoding="utf-8")
    inferred_target = target_date or infer_target_date_from_path(report_path) or infer_target_date_from_text(text)
    if not inferred_target:
        raise ValueError("Could not infer target date. Pass --target-date explicitly.")

    window = build_window(inferred_target, window_days=window_days)
    sections = parse_sections(text)
    checks = []

    missing_sections = [section for section in REQUIRED_SECTIONS if section not in sections]
    checks.append(
        make_check(
            "required_sections",
            not missing_sections,
            "All required sections are present." if not missing_sections else f"Missing sections: {missing_sections}",
            {"missing_sections": missing_sections},
        )
    )

    section_content_failures = []
    for section_name in REQUIRED_SECTIONS:
        body = sections.get(section_name, "")
        entries = split_entry_blocks(body)
        has_empty_notice = bool(NO_UPDATE_RE.search(body))
        if not entries and not has_empty_notice:
            section_content_failures.append(section_name)
    checks.append(
        make_check(
            "section_content_or_empty_notice",
            not section_content_failures,
            "Each section has entries or an explicit empty notice."
            if not section_content_failures
            else f"Sections without entries or empty notice: {section_content_failures}",
            {"invalid_sections": section_content_failures},
        )
    )

    entry_blocks: List[dict] = []
    url_failures = []
    source_date_url_failures = []
    for section_name, body in sections.items():
        for entry_index, block in enumerate(split_entry_blocks(body), start=1):
            urls = URL_RE.findall(block)
            source_date_url_links = SOURCE_DATE_URL_RE.findall(block)
            entry_id = f"{section_name}#{entry_index}"
            entry_blocks.append({"id": entry_id, "section": section_name, "text": block})
            if not urls:
                url_failures.append(entry_id)
            if not source_date_url_links:
                source_date_url_failures.append(entry_id)

    checks.append(
        make_check(
            "all_entries_have_urls",
            not url_failures,
            "Every entry includes at least one URL." if not url_failures else f"Entries missing URLs: {url_failures}",
            {"invalid_entries": url_failures},
        )
    )
    checks.append(
        make_check(
            "source_date_url_format",
            not source_date_url_failures,
            "Every entry includes a [source · date](url) citation."
            if not source_date_url_failures
            else f"Entries missing source/date/url citation: {source_date_url_failures}",
            {"invalid_entries": source_date_url_failures},
        )
    )

    date_strings = DATE_RE.findall(text)
    out_of_window = []
    for value in date_strings:
        parsed = parse_iso_date(value)
        if parsed < window.start_date or parsed > window.end_date:
            out_of_window.append(value)

    checks.append(
        make_check(
            "dates_within_window",
            not out_of_window,
            "All explicit dates fall within the allowed window."
            if not out_of_window
            else f"Out-of-window dates: {sorted(set(out_of_window))}",
            {"dates_found": date_strings, "out_of_window_dates": sorted(set(out_of_window))},
        )
    )

    model_section = sections.get("二、模型与研究", "")
    model_lower = model_section.lower()
    model_modality_present = any(keyword in model_lower for keyword in MODEL_MODALITY_KEYWORDS)
    model_ok = model_modality_present or bool(NO_UPDATE_RE.search(model_section))
    checks.append(
        make_check(
            "model_modality_coverage",
            model_ok,
            "Model section includes non-text modality coverage or explicit empty notice."
            if model_ok
            else "Model section lacks clear video/image/audio/multimodal coverage.",
        )
    )

    summary_present = "## 今日一句话总结" in text
    checks.append(
        make_check(
            "summary_section",
            summary_present,
            "Summary section is present." if summary_present else "Missing 今日一句话总结 section.",
        )
    )

    footer_ok = bool(re.search(r"\*生成时间：\d{4}-\d{2}-\d{2} .+收录范围：", text))
    checks.append(
        make_check(
            "footer_generation_and_range",
            footer_ok,
            "Footer includes generation time and coverage range."
            if footer_ok
            else "Missing footer generation time and/or coverage range.",
        )
    )

    return {
        "ok": all(check["passed"] for check in checks),
        "report_path": str(report_path),
        "target_date": inferred_target,
        "window_days": window_days,
        "window_start": window.start_date.isoformat(),
        "window_end": window.end_date.isoformat(),
        "sections_found": list(sections.keys()),
        "entry_count": len(entry_blocks),
        "checks": checks,
    }


def dump_validation(result: dict) -> str:
    return json.dumps(result, ensure_ascii=False, indent=2)
