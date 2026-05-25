# 信息源指南

## 信息源优先级

| 优先级 | 来源 | 类型 | 说明 |
|--------|------|------|------|
| 1 | 官方博客/新闻稿 | 核实 | 每条🔴必须核实 |
| 2 | VentureBeat / TechCrunch | 英文媒体 | 直接 webfetch |
| 3 | HuggingFace Papers | 学术模型 | 直接 webfetch |
| 4 | GitHub Trending | 开源社区 | 直接 webfetch |
| 5 | Reddit ML/LocalLLaMA | 社区讨论 | 直接 webfetch |
| 6 | Hacker News | 技术社区 | 直接 webfetch |
| 7 | 量子位 / 机器之心 / 36kr | 中文媒体 | librarian 搜索 |
| 8 | librarian 搜索 | 兜底 | 最后手段，必须核实日期 |

---

## 国际信息源（webfetch 直接抓取）

### 英文媒体
- `https://venturebeat.com/category/ai/`
- `https://techcrunch.com/category/artificial-intelligence/`

### 学术/开源
- `https://huggingface.co/papers/date/{YYYY-MM-DD}` — 当日论文
- `https://huggingface.co/papers/date/{YYYY-MM-DD-1}` — 前一天论文（HF 有刷新延迟，必须抓前一天作 fallback）
- `https://github.com/trending?since=daily` — AI/ML 日榜（⭐>200 的条目重点关注）
- `https://github.com/trending?since=weekly` — AI/ML 周榜（捕捉新晋高星项目，如 everything-claude-code；⭐>2000 标为🔴）
- `https://github.com/trending?since=daily&spoken_language_code=zh` — 中文项目日榜（补充国内开源动态）

### 社区
- `https://news.ycombinator.com` — 筛选 AI 相关帖子（👍>200 的条目重点关注）
- `https://old.reddit.com/r/MachineLearning/new/` — 优先用 old.reddit，噪声更低
- `https://old.reddit.com/r/LocalLLaMA/new/`
- `https://old.reddit.com/r/artificial/new/` — 更广泛 AI 社区讨论

### 国际模型公司官方博客（核实用）
| 公司 | 官方博客 |
|------|---------|
| OpenAI | https://openai.com/blog |
| Anthropic | https://www.anthropic.com/news |
| Google DeepMind | https://deepmind.google/discover/blog/ |
| Meta AI | https://ai.meta.com/blog/ |
| Mistral | https://mistral.ai/news/ |
| xAI | https://x.ai/blog |
| Stability AI | https://stability.ai/news |
| Runway | https://runwayml.com/blog |

---

## 国内信息源（librarian 搜索）

### librarian Agent C 指令 — 国内全模态模型/研究

```
搜索目标（文字模型）：
  阿里Qwen / 百度文心 / 字节豆包 / 智谱GLM / 月之暗面Kimi /
  DeepSeek / 小米MiMo / MiniMax / 阶跃星辰

搜索目标（视频/图像/音频模型）— 重点关注，英文媒体覆盖不足：
  昆仑万维SkyReels / 快手可灵 / 字节即梦 / 海螺AI /
  稳定扩散国内版 / 腾讯混元视频 / 阿里通义万象

来源：新浪科技 / 36kr / 量子位 / 机器之心 / 澎湃科技

关键词：
  AI 模型 发布 {YYYY}年{M}月{D}日
  视频生成 图像生成 {YYYY}年{M}月{D}日
  大模型 开源 {YYYY}年{M}月{D}日

必须确认：发布日期在 SEARCH_WINDOW 内，否则丢弃
格式：【来源 · 日期 · URL】标题 - 核心内容1句话 - 重要性(高/中)
```

### librarian Agent D 指令 — 业界变动

```
搜索目标：AI公司人事/融资/并购/合作/政策

关键词（英文）：
  "AI" "raises" OR "acquires" OR "partnership" OR "CEO" OR "layoffs" "{date}"
  "AI funding" "{YYYY-MM-DD}"

关键词（中文）：
  AI 融资 并购 合作 人事 {YYYY}年{M}月{D}日
  AI 裁员 战略 监管 {YYYY}年{M}月{D}日

来源：TechCrunch / Bloomberg / Reuters / 36kr / 量子位

必须确认：发布日期在 SEARCH_WINDOW 内，否则丢弃
格式：【来源 · 日期 · URL】标题 - 核心内容1句话 - 重要性(高/中)
```

### 国内公司官方博客（核实用）
| 公司 | 官方渠道 |
|------|---------|
| 阿里Qwen | https://qwen.ai/research |
| 百度文心 | https://yiyan.baidu.com |
| 昆仑万维SkyReels | https://skyreels.ai |
| 快手可灵 | https://kling.kuaishou.com |
| MiniMax | https://www.minimax.io/news |
| 小米MiMo | https://github.com/XiaomiMiMo |

---

## 已知局限

- 中文新闻源（36kr/微博）有时无法访问，国内动态可能有盲区
- **librarian 遇到 API 限速时会用历史知识填充，产生错误信息** — 必须用 webfetch 核实日期
- 视频生成模型（昆仑万维/快手/即梦）在英文媒体覆盖严重不足，必须专门用中文源补充
- X/Twitter 内容无法直接 webfetch，需通过 librarian 搜索
- 搜索 API 对当日极新内容（发布后数小时内）覆盖有延迟

---

## 国际形势与政治信息源

### 预测市场（核心源）
- **Polymarket** — `https://polymarket.com` — 真金白银的预测市场，覆盖地缘政治、选举、国际冲突
  - 搜索方式：通过 librarian 搜索 "Polymarket {事件关键词}" 或直接访问分类页面
  - 重点关注：地缘政治、美国政治、国际冲突、政策变化
  - 数据格式：事件名称 + 具体赔率 + 24h变化 + 交易量

### 国际新闻媒体
- **Reuters** — `https://www.reuters.com/world/` — 国际新闻权威源
- **BBC News** — `https://www.bbc.com/news/world` — 英国视角国际报道
- **Al Jazeera** — `https://www.aljazeera.com` — 中东视角国际报道
- **The Guardian** — `https://www.theguardian.com/world` — 深度国际报道
- **Financial Times** — `https://www.ft.com` — 金融与政治交叉报道

### 社区讨论
- `https://old.reddit.com/r/worldnews/new/` — 国际新闻讨论
- `https://old.reddit.com/r/geopolitics/new/` — 地缘政治分析
- `https://news.ycombinator.com` — 技术社区对国际事件的讨论

### 搜索策略
- **Polymarket 优先**：先搜索预测市场赔率，作为"真金白银"信号
- **媒体交叉验证**：同一事件在 Reuters + BBC + Polymarket 出现 → 🔴 高优先级
- **关注赔率变化**：24h 内赔率变化 >10% 的事件优先收录
- **避免纯观点**：优先收录有具体事实和数据支撑的报道

