import json
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = SKILL_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from report_validator import validate_report  # type: ignore  # noqa: E402


VALID_REPORT = textwrap.dedent(
    """\
    # AI 每日日报 · 2026年3月23日

    > 收录范围：3月21日 - 3月23日 · 每条标注来源与URL

    ---

    ## 一、基础设施与算力

    **🔴 AWS Trainium 扩容**
    训练基础设施继续增强。
    [TechCrunch · 2026-03-22](https://example.com/trainium)

    ---

    ## 二、模型与研究

    **🟡 视频生成工作流继续工具链化**
    视频生成模型继续升温。
    [GitHub Trending · 2026-03-23](https://example.com/video)

    ---

    ## 三、研究与社区

    **🟡 [example/repo](https://github.com/example/repo)** — 社区继续讨论，⭐230 today。
    [GitHub Trending · 2026-03-23](https://github.com/trending?since=daily)

    ---

    ## 四、业界变动

    **🟡 某公司达成合作**
    AI 公司合作加深。
    [Reuters · 2026-03-21](https://example.com/deal)

    ---

    ## 今日一句话总结

    > AI 竞争继续从模型能力走向产品化与基础设施化。

    ---

    *生成时间：2026-03-23 20:12 CST · 收录范围：3月21-23日*
    """
)


class CheckReportTests(unittest.TestCase):
    def write_report(self, content: str, filename: str = "2026-03-23-AI日报.md") -> Path:
        tempdir = Path(tempfile.mkdtemp())
        path = tempdir / filename
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_report_passes_core_checks(self) -> None:
        report_path = self.write_report(VALID_REPORT)

        result = validate_report(report_path, target_date="2026-03-23")

        self.assertTrue(result["ok"], json.dumps(result, ensure_ascii=False, indent=2))
        by_name = {check["name"]: check for check in result["checks"]}
        self.assertTrue(by_name["required_sections"]["passed"])
        self.assertTrue(by_name["all_entries_have_urls"]["passed"])
        self.assertTrue(by_name["dates_within_window"]["passed"])
        self.assertTrue(by_name["model_modality_coverage"]["passed"])

    def test_out_of_window_dates_fail(self) -> None:
        report_path = self.write_report(
            VALID_REPORT.replace("2026-03-21", "2026-03-18", 1)
        )

        result = validate_report(report_path, target_date="2026-03-23")

        self.assertFalse(result["ok"])
        by_name = {check["name"]: check for check in result["checks"]}
        self.assertFalse(by_name["dates_within_window"]["passed"])

    def test_missing_section_fails(self) -> None:
        report_path = self.write_report(VALID_REPORT.replace("## 四、业界变动", "## 四、其他内容"))

        result = validate_report(report_path, target_date="2026-03-23")

        self.assertFalse(result["ok"])
        by_name = {check["name"]: check for check in result["checks"]}
        self.assertFalse(by_name["required_sections"]["passed"])

    def test_missing_url_fails(self) -> None:
        report_path = self.write_report(
            VALID_REPORT.replace(
                "[Reuters · 2026-03-21](https://example.com/deal)",
                "[Reuters · 2026-03-21]",
            )
        )

        result = validate_report(report_path, target_date="2026-03-23")

        self.assertFalse(result["ok"])
        by_name = {check["name"]: check for check in result["checks"]}
        self.assertFalse(by_name["all_entries_have_urls"]["passed"])


if __name__ == "__main__":
    unittest.main()
