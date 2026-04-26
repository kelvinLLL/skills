#!/usr/bin/env python3

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional

from report_validator import dump_validation, infer_target_date_from_path, infer_target_date_from_text, validate_report


def load_eval_case(eval_file: Path, eval_id: int) -> dict:
    payload = json.loads(eval_file.read_text(encoding="utf-8"))
    for item in payload.get("evals", []):
        if item.get("id") == eval_id:
            return item
    raise ValueError(f"Eval id {eval_id} not found in {eval_file}")


def extract_target_date(prompt: str, report_path: Path) -> Optional[str]:
    return infer_target_date_from_text(prompt) or infer_target_date_from_path(report_path)


def expectation_result(expectation: str, validator: dict, report_path: Path, target_date: str) -> dict:
    checks = {item["name"]: item for item in validator["checks"]}
    passed = None
    detail = ""

    if "输出文件名包含" in expectation:
        passed = target_date in report_path.name
        detail = f"Report filename is {report_path.name}."
    elif "四个板块" in expectation:
        passed = checks["required_sections"]["passed"]
        detail = checks["required_sections"]["detail"]
    elif "每个板块至少有1条条目或明确写明" in expectation:
        passed = checks["section_content_or_empty_notice"]["passed"]
        detail = checks["section_content_or_empty_notice"]["detail"]
    elif "每条条目包含来源名称、日期和URL" in expectation or "每条条目包含URL" in expectation:
        passed = checks["source_date_url_format"]["passed"]
        detail = checks["source_date_url_format"]["detail"]
    elif "所有条目的日期在" in expectation or "不含日期早于" in expectation:
        passed = checks["dates_within_window"]["passed"]
        detail = checks["dates_within_window"]["detail"]
    elif "今日一句话总结" in expectation:
        passed = checks["summary_section"]["passed"]
        detail = checks["summary_section"]["detail"]
    elif "生成时间和收录范围" in expectation:
        passed = checks["footer_generation_and_range"]["passed"]
        detail = checks["footer_generation_and_range"]["detail"]
    elif "独立的'业界变动'板块" in expectation:
        passed = checks["required_sections"]["passed"]
        detail = checks["required_sections"]["detail"]
    elif "非文字LLM" in expectation or "视频或图像生成模型" in expectation:
        passed = checks["model_modality_coverage"]["passed"]
        detail = checks["model_modality_coverage"]["detail"]
    else:
        passed = False
        detail = "No mechanical mapping implemented yet for this expectation."

    return {
        "expectation": expectation,
        "passed": bool(passed),
        "supported": "No mechanical mapping" not in detail,
        "detail": detail,
    }


def grade_report_against_eval(eval_file: Path, eval_id: int, report_path: Path) -> dict:
    eval_case = load_eval_case(eval_file, eval_id)
    target_date = extract_target_date(eval_case.get("prompt", ""), report_path)
    if not target_date:
        raise ValueError("Could not infer target date from eval prompt or report filename.")

    validator = validate_report(report_path, target_date=target_date)
    expectation_checks = [
        expectation_result(expectation, validator, report_path, target_date)
        for expectation in eval_case.get("expectations", [])
    ]
    passed_count = len([item for item in expectation_checks if item["passed"]])

    return {
        "eval_id": eval_id,
        "prompt": eval_case.get("prompt", ""),
        "report_path": str(report_path),
        "target_date": target_date,
        "validator": validator,
        "expectation_checks": expectation_checks,
        "summary": {
            "validator_ok": validator["ok"],
            "passed_expectations": passed_count,
            "total_expectations": len(expectation_checks),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Grade a report against an ai-daily-report eval case.")
    parser.add_argument("--eval-file", required=True, help="Path to evals.json")
    parser.add_argument("--eval-id", required=True, type=int, help="Eval case id")
    parser.add_argument("--report", required=True, help="Path to the generated report markdown")
    args = parser.parse_args()

    result = grade_report_against_eval(Path(args.eval_file), args.eval_id, Path(args.report))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["validator"]["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
