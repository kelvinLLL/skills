import json
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = SKILL_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from grade_eval import grade_report_against_eval  # type: ignore  # noqa: E402


REPORT = textwrap.dedent(
    """\
    # AI 每日日报 · 2026年3月19日

    > 收录范围：3月17日 - 3月19日 · 每条标注来源与URL

    ---

    ## 一、基础设施与算力

    **🔴 某基础设施新闻**
    摘要。
    [TechCrunch · 2026-03-18](https://example.com/infra)

    ---

    ## 二、模型与研究

    **🟡 视频生成模型继续活跃**
    摘要。
    [量子位 · 2026-03-19](https://example.com/video)

    ---

    ## 三、研究与社区

    **🟡 [foo/bar](https://github.com/foo/bar)** — 热门项目继续上升，⭐500 today。
    [GitHub Trending · 2026-03-19](https://github.com/trending?since=daily)

    ---

    ## 四、业界变动

    **🟡 融资合作事件**
    摘要。
    [Reuters · 2026-03-18](https://example.com/business)

    ---

    ## 今日一句话总结

    > 今日最大信号是多模态和基础设施一起推进。

    ---

    *生成时间：2026-03-19 20:12 CST · 收录范围：3月17-19日*
    """
)


class GradeEvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = Path(tempfile.mkdtemp())
        self.report_path = self.tempdir / "2026-03-19-AI日报.md"
        self.report_path.write_text(REPORT, encoding="utf-8")

        self.eval_file = self.tempdir / "evals.json"
        self.eval_file.write_text(
            json.dumps(
                {
                    "skill_name": "ai-daily-report",
                    "evals": [
                        {
                            "id": 1,
                            "prompt": "生成今日日报（2026年3月19日）",
                            "expected_output": "生成日报文件并满足基础格式。",
                            "expectations": [
                                "输出文件名包含 2026-03-19",
                                "日报包含四个板块：基础设施与算力、模型与研究、研究与社区、业界变动",
                                "每条条目包含来源名称、日期和URL（格式：[来源 · YYYY-MM-DD](URL)）",
                                "所有条目的日期在2026-03-17至2026-03-21范围内，不含更早的历史内容",
                                "日报末尾包含'今日一句话总结'",
                                "日报末尾标注生成时间和收录范围",
                            ],
                        }
                    ],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    def test_grade_report_against_eval_returns_summary_and_checks(self) -> None:
        result = grade_report_against_eval(self.eval_file, 1, self.report_path)

        self.assertEqual(result["eval_id"], 1)
        self.assertEqual(result["target_date"], "2026-03-19")
        self.assertIn("validator", result)
        self.assertIn("expectation_checks", result)
        self.assertTrue(any(item["passed"] for item in result["expectation_checks"]))

    def test_grade_report_flags_failed_expectation(self) -> None:
        broken_path = self.tempdir / "2026-03-19-AI日报-broken.md"
        broken_path.write_text(REPORT.replace("## 四、业界变动", "## 四、其他"), encoding="utf-8")

        result = grade_report_against_eval(self.eval_file, 1, broken_path)

        failed = [item for item in result["expectation_checks"] if not item["passed"]]
        self.assertTrue(failed, json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    unittest.main()
