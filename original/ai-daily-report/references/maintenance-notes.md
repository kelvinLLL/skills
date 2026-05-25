# AI Daily Report Skill 维护与调研笔记

## 目的

这份文档面向维护 `ai-daily-report` skill 的人，而不是面向每次生成日报时的执行者。

记录三类信息：

1. `agents/openai.yaml` 的作用和维护规则
2. 公开可参考的相似 skill / 近似工作流
3. 下一阶段工程化改进建议

---

## 为什么补 `agents/openai.yaml`

`agents/openai.yaml` 是给产品界面和运行时 harness 读的，不是给模型触发 skill 用的。

- `SKILL.md` frontmatter 中的 `name` 和 `description` 仍然是主要触发机制
- `agents/openai.yaml` 主要补充 UI 展示和默认调用体验
- 常见字段包括：
  - `display_name`：技能在列表里的展示名
  - `short_description`：短描述，便于快速扫描
  - `default_prompt`：在显式调用 skill 时可插入的示例提示词
- 只有在明确提供图标或品牌色时，才需要补 `icon_*` 或 `brand_color`

本地规范参考：

- `/Users/haojunliu/.codex/skills/.system/skill-creator/references/openai_yaml.md`
- `/Users/haojunliu/.codex/skills/.system/openai-docs/agents/openai.yaml`
- `/Users/haojunliu/.codex/vendor_imports/skills/skills/.curated/notion-research-documentation/agents/openai.yaml`

对本 skill 的实际意义：

- 让 `ai-daily-report` 在技能列表中更容易被发现
- 给显式调用提供更稳定的默认提示词
- 把“面向用户的技能包装”与“面向模型的执行说明”分离

---

## 公开相似 Skill / 近似工作流

结论先行：公开可见的“新闻/日报编辑型 skill”非常少，最接近的不是完整 AI 日报 skill，而是“每日趋势收集”和“每日活动总结”两类。

### 1. `neta-trend-daily`

- 来源：<https://gist.github.com/hand-dot/bf6f928dce14095d5eef4f6aae63275e>
- 类型：每日趋势收集 skill
- 公开信息显示它会收集 Hatena Bookmark IT 热门条目和 Hacker News 热门文章，并保存到按日期命名的日报文件

可借鉴点：

- 有固定源，而不是开放式“随便搜”
- 明确写入日期化产物路径
- 先收集再整理，目标交付物非常清晰

与本 skill 的差异：

- 它更像“趋势素材采集器”
- 本 skill 更强调多来源核实、中文补盲、四板块编辑整合

### 2. `today-in-claude-code`

- 来源：<https://gist.github.com/chrismdp/29b3c5504504fe9ad2ff3310fa2a2a99>
- 类型：每日活动总结 skill
- 公开说明里要求先读取权威数据源（`npx ccusage --today` 和本地历史记录），再做主题归纳和日报化输出

可借鉴点：

- 先取“权威原始数据”，再做摘要
- 工作流分层清楚：采集 -> 分组 -> 提炼 -> 固定格式输出
- 明确区分“重要主题”和“Other”，降低琐碎信息污染

与本 skill 的差异：

- 它的数据源是本地日志，确定性强
- 本 skill 面向外部新闻源，难点在时效性、去重和真实性核验

### 3. `claude-skills-base` 中的结构参考

- 来源：<https://github.com/Cam10001110101/claude-skills-base>
- 这不是日报 skill，但它展示了几种值得借鉴的技能包装模式：
  - `internal-comms/` 带有 newsletter / FAQ / update templates
  - `mcp-builder/` 同时包含 reference、scripts 和 evaluation 相关结构

可借鉴点：

- 复杂 skill 可以把“模板、参考资料、脚本、评估”拆成不同目录
- 维护型材料不一定写进主 `SKILL.md`

### 为什么没有找到更多高度相似的公开 skill

我目前没有找到成熟、公开、且与“AI 行业每日日报”高度同构的 skill 仓库。更常见的公开 skill 主要集中在：

- 编码和代码审查
- MCP / API / 文档处理
- 个人工作流总结

这意味着 `ai-daily-report` 目前更像一个少见的“编辑型 skill”，不是已有通用模板的简单套壳。

---

## 可提炼的成熟实践

### 1. 先定义成功标准，再做 prompt 调整

Anthropic 的 prompt engineering 总览明确要求先有成功标准、经验性测试方法和第一版 prompt，再进入迭代。

参考：

- <https://docs.anthropic.com/en/docs/prompt-engineering>

对本 skill 的含义：

- “是否像日报”不是唯一标准
- 还要可检验地满足：日期窗口、URL 完整性、板块覆盖、模态覆盖、重要性区分、去重

### 2. 评测流程要包含目标、数据集、指标和版本对比

OpenAI 的 evaluation best practices 把 eval 流程拆成：

1. 定义目标
2. 收集数据集
3. 定义指标
4. 跑对比并迭代

Anthropic 的 Evaluation Tool 也强调：

- side-by-side comparison
- quality grading
- prompt versioning

参考：

- <https://developers.openai.com/api/docs/guides/evaluation-best-practices>
- <https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool>

对本 skill 的含义：

- 现在的 `evals/evals.json` 已经有“目标”和“部分指标”
- 下一步缺的是真实运行产物、打分记录和版本对比

### 3. 结构化中间产物比纯 Markdown 更利于校验

OpenAI Structured Outputs 官方指南建议用 JSON Schema 约束模型输出，并明确建议：

- key 要命名清晰
- 给重要字段写清描述
- 用 eval 来验证结构是否适合当前任务

参考：

- <https://developers.openai.com/api/docs/guides/structured-outputs>

对本 skill 的含义：

与其直接从搜索结果跳到 Markdown 日报，更稳定的工程化路径是：

1. 先产出结构化条目列表
2. 再做 Markdown 排版

建议的中间条目结构：

```json
{
  "title": "事件标题",
  "section": "基础设施与算力",
  "priority": "red",
  "source_name": "TechCrunch",
  "published_at": "2026-03-22",
  "url": "https://...",
  "verification_status": "official_confirmed",
  "modality": ["llm", "video"],
  "summary": "一句话摘要",
  "evidence_excerpt": "用于人工核对的原句或要点"
}
```

这样后续的日期窗口检查、URL 必填检查、板块统计、🔴/🟡 分布检查都更好做。

### 4. Prompt 结构要显式分层

Anthropic 文档建议把复杂提示拆进 XML 标签中，把 instruction、context、documents、input 分开，并在长上下文任务中优先把材料放前面、问题放后面。

参考：

- <https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags>

对本 skill 的含义：

如果未来把日报生成半自动化，可以把主 prompt 拆成：

```xml
<goal>生成目标日期的 AI 每日日报</goal>
<date_window>2026-03-21 to 2026-03-23</date_window>
<quality_rules>...</quality_rules>
<candidate_items>...</candidate_items>
<output_template>...</output_template>
```

这样比把所有规则堆成一段自然语言更稳，也更适合版本迭代。

### 5. “可引用”能力的本质是把证据留在结构里

Anthropic 的 citations 文档强调：引用的价值不只是“看起来有出处”，而是让 claim 能追溯到具体证据块，并且引用粒度可控。

参考：

- <https://docs.anthropic.com/en/docs/build-with-claude/citations>

对本 skill 的含义：

虽然当前日报主要基于网页和新闻源，不是直接喂文档 API，但思路可以迁移：

- 每条日报项都要保留来源名、日期、URL
- 高优先级项最好保留“官方核实来源 + 媒体来源”双证据
- 后续若做自动化，应保留原始摘录或结构化 evidence，而不是只留最终 prose

---

## 对 `ai-daily-report` 的具体建议

### 这轮已经做的

- 保留新版 `skills/original/ai-daily-report/`
- 删除旧版重复 skill
- 增加 `agents/openai.yaml`
- 补一份面向维护者的调研与工程化说明
- 增加 `scripts/check_report.py`、`scripts/report_validator.py` 和 `scripts/grade_eval.py`
- 增加对应单元测试：`tests/test_check_report.py`、`tests/test_grade_eval.py`

### 当前工具

#### 1. `scripts/check_report.py`

用途：对最终 Markdown 日报做机械校验。

当前已覆盖：

- 文件名日期推断或显式传入 `--target-date`
- 四个目标板块检查
- 每个板块有条目或“暂无动态”说明
- 每条目 URL 检查
- `[来源 · YYYY-MM-DD](URL)` 格式检查
- 日期窗口检查
- 模型板块非文字模态覆盖检查
- 总结段落和页脚检查

示例：

```bash
python3 skills/original/ai-daily-report/scripts/check_report.py 2026-03-23-AI日报.md --target-date 2026-03-23
```

#### 2. `scripts/grade_eval.py`

用途：把单个日报文件与 `evals/evals.json` 中的某个 eval case 对齐，输出 JSON grading 结果。

当前做法：

- 读取 `eval_id`
- 从 eval prompt 或文件名推断目标日期
- 先调用 validator
- 再把常见 expectation 映射到机械检查

示例：

```bash
python3 skills/original/ai-daily-report/scripts/grade_eval.py \
  --eval-file skills/original/ai-daily-report/evals/evals.json \
  --eval-id 1 \
  --report 2026-03-19-AI日报-v3.md
```

注意：

- 旧产物若仍采用历史板块名（如“应用与商业”），grader 会明确打出失败项
- 这是预期行为，说明它已经能识别“skill 规范”和“历史产物”之间的脱节

### 下一轮优先级最高的事情

#### 1. 增加结构化中间文件

建议在未来运行时额外保存：

- `artifacts/YYYY-MM-DD-items.json`

用途：

- 给 `check_report.py` 提供更稳定的输入
- 给未来的 eval grader 提供可读证据
- 便于做去重与覆盖统计

#### 2. 让 eval 从“规格文件”变成“运行闭环”

当前已有：

- `evals/evals.json`
- `scripts/grade_eval.py`
- `eval-viewer/`

下一步缺失：

- 每次 eval run 的 `outputs/`
- grading 结果
- 基线与新版本对比

建议闭环：

1. 读取单条 eval prompt
2. 生成日报文件和中间 JSON
3. 运行校验器生成 `grading.json`
4. 用 `eval-viewer` 查看结果并记录人工反馈

---

## 维护判断

这套 skill 现在的强项不是“完全自动化”，而是“编辑判断力 + 抗幻觉经验”。

因此演进路线应当是：

1. 继续保留简洁的主 `SKILL.md`
2. 把工程化能力沉到 `references/`、`scripts/`、`evals/`
3. 先补“可验证性”，再补“自动化程度”

不建议当前就拆成多个子 skill。证据还不够，容易提前复杂化。
