---
name: stock-research
description: Use when researching a public company or stock for an investment decision - analyzing a ticker, reading financial statements, estimating fair value, judging whether a stock is cheap or expensive, comparing a company to peers, or gauging community sentiment on an equity.
---

# Stock Research

## Overview

A disciplined workflow for fundamental equity research. **Core principle: present first-hand data with sources and timestamps; let the investor judge. You analyze, you do not decide for them.**

The danger is not lack of data - it is acting on stale, second-hand, or single-source numbers and presenting conclusions instead of evidence. This skill exists to prevent that.

## When to Use

- "Research / analyze {ticker or company}", "is {stock} cheap?", "read {company}'s financials"
- Estimating fair value / PE, judging an earnings report, comparing peers
- Gauging what people say about a stock

**Not for:** real-time trading signals, technical-chart timing, or portfolio allocation math.

## The 7 Principles (the constitution)

1. **First-hand first, judge before you borrow** - pull raw data and form your own read BEFORE reading sell-side/media opinions (avoids anchoring bias).
2. **Present, don't summarize away** - always show the raw numbers + source + timestamp. The investor holds final judgment.
3. **Tier your sources** - the further from the filing, the more you discount it (see table).
4. **Timestamp and basis** - every number gets a date and a basis (GAAP net vs 扣非/non-recurring, TTM vs annual). A number with no date is untrusted.
5. **Cross-check, and the anchor must be fresh** - verify with identities (`market cap = price × shares`, `EPS = net income / shares`, `OCF/NI`, `receivables growth vs revenue growth`). When two numbers conflict, do NOT assume the one matching your other (possibly stale) number is right - fetch a fresh authoritative value.
6. **Disconfirm on purpose** - after forming a thesis, actively hunt the bear case.
7. **Noise-robust conclusions** - when data conflicts, lead with judgments that hold across every version of the numbers.

## Workflow (5 steps)

1. **Frame** - what decision (buy/hold/sell), what horizon? Horizon sets track weights (short-term: catalysts/flows; long-term: moat/ROE).
2. **First-hand → independent analysis** - quantitative (3 statements + F10 key metrics) and qualitative (filings, MD&A, earnings-call notes). Analyze before reading others.
3. **Second-hand → mark the disagreements** - read broker/industry reports; explicitly flag where they agree vs disagree with your first-hand read. Disagreements are where the alpha (or your blind spot) hides.
4. **Synthesize one version** - bull/bear, with an explicit disconfirmation/bear-case section.
5. **Present everything, layered and sourced** - first-hand data + second-hand views + your analysis, each traceable with source and timestamp. Investor decides.

## Deliverables (bilingual, mandatory when saving)

When asked to save/produce a research brief, deliver **TWO files: a full English version and a full Chinese version (完整中文版)**. The Chinese version is a **complete parallel report - NOT a condensed summary**: same sections, same depth, same tables, same numbers; only prose and section headers are translated.

- Keep numbers, tickers, dates, and source URLs **identical** across both files; translate only the language.
- Filenames and headers must state the producing identity + `stock-research` skill + ticker + date, and mark the language pair (e.g. `..._英文版_...` / `..._中文版_...`).
- Both versions carry the live-price caveat and the "decision is yours; I present the evidence" framing.
- Save both under the investor's chosen folder.

## Analysis Tracks

Qualitative: **business model & moat** · **industry & cycle position** · **competitors & comps** · **governance / management / shareholders** (insider buy-sell, incentives, dividends)
Quantitative: **financials** (3 statements + water-check red flags) · **profitability & returns** (ROE DuPont) · **valuation**
Forward: **catalysts & expectation gaps** (next 12 months, what is unpriced) · **risks & disconfirmation**
Sentiment: **invoke the `last30days` skill** for English social/community sentiment (Reddit/X/YouTube/HN/web).
Optional: capital flows / positioning (short-term only).

> **Sentiment limitation - do not fabricate:** `last30days` has no reliable Chinese-platform coverage (only experimental Xiaohongshu). For **A-shares (`6xxxxx.SH` / `0/3xxxxx.SZ`), sentiment is currently a gap** - say so plainly; do not present meme/off-topic results as signal. (For A-share retail mood the investor checks Xueqiu / Eastmoney guba / iFinD manually.)

## Source Reliability Tiers

| Tier | Source | Use |
|---|---|---|
| ★★★★★ | Filings/announcements (cninfo/巨潮, exchanges), earnings-call transcripts | final basis |
| ★★★★ | F10 (Eastmoney/Tonghuashun), Wind/Choice, stockanalysis.com (S&P backed) | fast pull of statements, 扣非, consensus |
| ★★★ | Broker research PDFs, industry reports | framing, forecasts, cross-check |
| ★★ | Investing.com / GuruFocus / aggregators | rough only - numbers often stale/garbled |
| ★ | Search-engine snippets, media retellings | leads only - never trust the number |

**Live price: the investor's terminal beats your WebSearch/WebFetch. Ask for or accept their live quote; you analyze.**

**A-share data access (recurring gap):** Xueqiu and Eastmoney/Tonghuashun F10 pages are JS-rendered and usually NOT parseable by WebFetch, so segment mix, 扣非, and shareholder/insider detail often go missing. Fallbacks, in order: (1) **cninfo / 巨潮 filing PDFs** (★★★★★, usually parseable) for 扣非, segments, shareholders, insider changes; (2) ask the investor to paste the F10 numbers; (3) if neither works, **explicitly state the governance / shareholder track is thin** - never skip it silently or fabricate it.

## Valuation Quick Reference

- `P = EPS × PE`. Growth stocks: use **forward PE**, not trailing.
- Fair-PE anchors: **PEG** (≈1 baseline) · historical PE percentile · peer comps · price-implied growth · lifecycle/certainty.
- **Cyclical trap:** at peak earnings, low PE is dangerous (E is about to fall); use normalized earnings + PB + cycle position.
- Beat → first **raises EPS forecast** (price up at constant PE); PE expands only if durability/certainty re-rates (Davis double-play).

Deep detail + worked example: see `references/financial-analysis.md`.

## Reading Financials: water-check red flags

Three cross-validating flags (one = caution; two reinforcing = near-confirmed):
1. **Net income up but OCF lagging** (OCF/NI < 1)
2. **Receivables growth ≫ revenue growth** (profit became IOUs)
3. **Inventory growth ≫ revenue growth** (unsold buildup)

Plus: gross margin and net margin rising together = high-quality growth. Compare **归母 vs 扣非** (GAAP vs non-recurring) - large gap = one-off-driven, low quality.

## Common Mistakes (from real baseline failures)

| Mistake | Fix |
|---|---|
| Reaching for `last30days` on an A-share | A-share social = gap; rely on filings + broker research, state the gap |
| Quoting a price/market cap with no date | Timestamp everything; get a fresh live quote |
| Using a stale number as the anchor to "debunk" a fresh one | Cross-check only with fresh authoritative values |
| Trusting one aggregator's consensus target | Aggregators drift; for consensus use Wind/Choice/F10; treat conflicting pulls as low-confidence |
| Presenting a conclusion instead of the raw data | Show numbers + source + timestamp; let the investor judge |
| Skipping the bear case | Step 4 requires explicit disconfirmation |

## Red Flags - STOP

- About to state a stock price without a date → get a fresh one
- About to call a stock cheap/expensive on trailing PE for a cyclical → use forward + cycle position
- About to cite a single source for a key number → cross-check or label low-confidence
- About to give a verdict without showing the underlying data → present first, judge second
