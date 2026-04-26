---
name: ai-daily-report
description: >
  生成AI行业每日日报，覆盖AI全链路四个板块：基础设施与算力、模型与研究（全模态）、研究与社区、业界变动。
  当用户说"生成今日日报"、"做一份AI日报"、"daily report"、"今天AI有什么新动态"、
  "帮我看看今天AI圈发生了什么"、"出一期日报"时触发。
  即使用户没有明确说"日报"，只要意图是了解当日AI行业动态并输出结构化报告，就应该使用此skill。
  注意：日报只收录目标日期±2天内的新鲜内容，绝不用历史内容填充。
---

# AI Daily Report

生成一份严格当日的 AI 全链路日报。覆盖基础设施/模型（全模态）/研究社区/业界变动四个板块，每条标注来源与 URL。

## 核心原则

1. **日报 = 今日新鲜事**：只收录 TARGET_DATE ±2 天内的内容，超出窗口直接丢弃
2. **宁缺毋滥**：找不到今日内容 → 写"今日暂无重大动态"，绝不用历史内容填充
3. **直接抓取优先**：webfetch 主流媒体首页 > librarian（librarian 限速时会用历史知识填充，产生错误信息）
4. **官方核实**：每条 🔴 高优先级条目必须 webfetch 官方博客/新闻稿二次确认日期
5. **全模态覆盖**：视频/图像/音频生成模型与文字模型同等重要，参见 `references/sources.md` 中的国内视频模型列表
6. **每条必须有 URL**：格式 `[来源 · YYYY-MM-DD](URL)`，无法确认 URL 的条目降级或移除
7. **最低条数要求**：每个板块至少 5 条，目标 8-10 条；条数不足时必须扩大搜索范围，不得以"今日暂无"敷衍
8. **重要性必须区分**：每个板块至少 1 条 🔴，不得全部标为 🟡；🔴/🟡 判断标准见下方
9. **跨源收敛检测**：同一事件在 3+ 源出现（如 TechCrunch + HN + Reddit）自动升级为 🔴；跨源信号是最强证据

## 重要性判断标准

| 级别 | 标准 | 典型例子 |
|------|------|---------|
| 🔴 高 | 满足以下任一：① 头部公司（OpenAI/Anthropic/Google/Meta/字节/阿里/百度）重大发布；② 开源模型性能突破 SOTA；③ 融资金额 ≥ $100M 或重大并购；④ GitHub 新晋项目当日 ⭐ > 500 或周榜 ⭐ > 2000；⑤ 影响行业格局的政策/监管变化；⑥ **跨源收敛**：同一事件在 3+ 源出现（TechCrunch + HN + Reddit 等） | GPT-5 发布、Llama 4 开源、$500M 融资、多平台热议事件 |
| 🟡 中 | 值得关注但不满足🔴标准：中小公司产品更新、社区热门讨论、技术趋势信号、GitHub 日榜 ⭐ 200-500 | 新工具发布、社区讨论热帖、中型融资 |

**跨源收敛检测规则：**
- 同一事件在 TechCrunch/VentureBeat + HN + Reddit 中任意 3 源出现 → 自动升级为 🔴
- 判断标准：标题关键词重叠 > 60% 或核心实体相同（公司名/产品名/人名）
- 优先级：跨源信号 > 单源高互动 > 单源低互动

## 执行流程

### Step 0 — 确定日期与背景

```
TARGET_DATE = 用户指定日期，或默认今天
SEARCH_WINDOW = TARGET_DATE ±2 天
```

如工作目录有过去日报文件（`{date}-AI日报*.md`），读取最近 3 天，提取关键词作为搜索背景（不直接输出到日报）。

### Step 1 — 并行抓取

详细信息源列表见 `references/sources.md`。

同时启动以下任务（全部后台并行）：

**A. webfetch 英文媒体**（直接抓取，无限速风险）
- `https://venturebeat.com/category/ai/`
- `https://techcrunch.com/category/artificial-intelligence/`
- `https://huggingface.co/papers/date/{YYYY-MM-DD}`
- `https://huggingface.co/papers/date/{YYYY-MM-DD-1}`
- `https://news.ycombinator.com`（筛选 AI 相关）

**B. webfetch 社区源**（直接抓取）
- `https://github.com/trending?since=daily`（日榜，筛选 AI/ML 仓库）
- `https://github.com/trending?since=weekly`（周榜，捕捉新晋高星项目，如 everything-claude-code 类）
- `https://github.com/trending?since=daily&spoken_language_code=zh`（中文项目日榜）
- `https://old.reddit.com/r/MachineLearning/new/`（优先用 old.reddit，噪声更低）
- `https://old.reddit.com/r/LocalLLaMA/new/`
- `https://old.reddit.com/r/artificial/new/`（补充更广泛 AI 社区讨论）
- X/Twitter 搜索（可选，需配置 AUTH_TOKEN + CT0 或 XAI_API_KEY）：搜索 AI 行业关键账号和话题标签

**C. librarian — 国内全模态模型**（后台，补充中文源）
- 搜索目标、关键词、来源见 `references/sources.md` 的"国内信息源"章节

**D. librarian — 业界变动**（后台，补充融资/人事/政策）
- 搜索目标、关键词、来源见 `references/sources.md` 的"业界变动"章节

**E. librarian — 国际形势与政治**（后台，补充地缘政治/预测市场）
- 优先搜索 Polymarket 预测市场赔率（地缘政治、选举、国际冲突）
- 补充 Reuters、BBC、Al Jazeera 等国际新闻
- 搜索目标、关键词、来源见 `references/sources.md` 的"国际形势与政治信息源"章节

### Step 2 — 核实高优先级条目

对每条 🔴 条目：
1. webfetch 官方博客/新闻稿，确认发布日期在 SEARCH_WINDOW 内
2. 日期不符 → 降级为 🟡 或移除
3. 无法找到官方 URL → 降级为 🟡，标注"来源待核实"

### Step 3 — 整合输出

按 `references/output-template.md` 中的模板生成日报，保存至 `{workdir}/{YYYY-MM-DD}-AI日报.md`。

### Step 4 — 更新 insights

在工作目录的 `insights.md` 追加本次实践记录（格式见 `references/output-template.md` 末尾）。

## 维护参考

- `references/sources.md`：当需要扩展信息源、调整抓取优先级或补充中文/多模态覆盖时读取
- `references/output-template.md`：当需要调整日报模板、质量规则或 `insights.md` 追加格式时读取
- `references/maintenance-notes.md`：当需要更新 skill 包装、评估策略、校验脚本路线或查看外部同类 skill 参考时读取

<!-- Skill Supervisor Footer -->
## Skill Supervisor Footer

When this supervised skill is used, append one sanitized JSONL record to `~/.codex/skill-supervisor/usage.jsonl`.

Suggested record:

```json
{"timestamp":"<ISO-8601 UTC>","skill": "ai-daily-report","workspace":"<workspace basename or unknown>","trigger":"<short non-sensitive reason>","task_type":"<planning|implementation|review|research|other>","outcome":"<started|completed|blocked|skipped>","verification":"<passed|failed|not_run|not_applicable>"}
```

Only record metadata. Do not record secrets, credentials, full prompts, file contents, private user data, or long task transcripts. If logging is unavailable, continue the task normally.

If the `skill-supervisor` skill is installed globally, prefer its helper script:

```bash
python3 ~/.codex/skills/skill-supervisor/scripts/log_usage.py --skill "ai-daily-report" --trigger "<short non-sensitive reason>" --task-type "<type>" --outcome "<outcome>" --verification "<status>"
```
