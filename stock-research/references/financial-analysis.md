# Financial Analysis & Valuation - Reference

Deep detail for the `stock-research` skill. Read when actually computing valuation or dissecting an earnings report.

## Core identities

```
P (price)   = EPS × PE
Market cap  = Net income × PE  = Price × Shares outstanding
EPS         = Net income ÷ Shares outstanding
```

Use these to cross-check any quoted figure. Example sanity check: if market cap and share count imply a price far from the quoted price, **one input is stale** - fetch a fresh, timestamped authoritative value rather than trusting whichever matches your other (possibly stale) number.

## Reading the three statements

**Income statement** - revenue, gross/operating/net margin trend, EPS.
- Gross margin ↑ AND net margin ↑ → high-quality growth (pricing power / mix), not cost-cutting.
- Gross ↑ but net ↓ → cost/expense blowout (revenue up, profit not).
- Gross flat but net ↑ → cost discipline (slightly lower quality than pricing-driven).

**Cash flow** - the quality check.
- **OCF/NI (net-cash ratio):** >1 = profit backed by real cash; <1 = profit stuck on paper (usually receivables).
- **FCF = OCF − Capex.** Big capex in an expansion phase is fine *if OCF covers it and debt is not ballooning*.
- **Cash-collection ratio = "cash received from sales" ÷ revenue** (>1 ideal) - from the F10 cash-flow statement.

**Balance sheet** - ratios and trends, not absolute levels.
- Inventory: compare growth to revenue growth. Inventory growth ≫ revenue growth = unsold buildup.
- Receivables: receivables growth ≫ revenue growth = profit turning into IOUs (pairs with OCF/NI < 1).
- Leverage: `debt ratio = (total assets − equity) / total assets`. Low + falling debt supports a higher PE (certainty premium).

## 扣非 / non-recurring (A-share specific)

`扣非净利润 = 归母净利润 − 非经常性损益` (government subsidies, investment/disposal gains, fair-value changes, non-operating items).
- 归母 ≈ 扣非 → operating-driven, high quality.
- 归母 ≫ 扣非 → propped up by one-offs, low quality, unsustainable.
- 扣非 > 归母 → one-off losses masked a stronger core.
- Source: Eastmoney F10 → 主要指标 (international datasets omit this line).

## Estimating a reasonable PE (judgment, not a formula)

Five mutually-checking anchors:
1. **PEG** = PE ÷ growth%; ≈1 baseline for growth names. Always forward, not trailing.
2. **Historical PE percentile** - where current PE sits in the company's own range (lixinger / Eastmoney PE-band).
3. **Peer comps** - sector median PE as anchor.
4. **Price-implied growth** - back out the growth the current price assumes; judge if achievable. Converts a valuation call into a growth call.
5. **Lifecycle / certainty** - growth + high certainty earns a high PE; mature / low-visibility earns a low one.

**Cyclical reversal (critical):** for cyclical-growth names, peak-earnings = low PE is a *trap* (E about to fall); trough-earnings = high PE may be the buy. Use normalized (through-cycle) earnings, or PB + cycle position, instead of spot PE.

## How a beat flows into price

- **Path A (most common): estimate upgrade.** Beat → analysts raise future EPS → at constant PE, `P = EPS↑ × PE` rises. This is the real engine of most "beat → rally".
- **Path B: multiple expansion.** Market re-rates growth durability/certainty → higher PE.
- **A + B = Davis double-play** (surge). Miss + de-rating = Davis double-kill.
- Precise statement: a beat *first* raises the EPS forecast; whether PE expands depends on the durability and certainty of the growth, not automatically.

## Earnings-expectation mechanics (A-share)

- Disclosure calendar: Q1 by 4/30, interim/H1 by 8/31 (**pre-announcement 业绩预告 often in July**), Q3 by 10/31, annual by next 4/30.
- **业绩预告 / pre-announcement:** the first price reaction usually happens here, not at the formal report.
- **Expectation gap drives price**, not absolute results: in-line ≈ flat; beat → up *only if structural and 扣非-backed*; miss → down (distinguish one-off vs core deterioration).

## Worked-example template

Given: live price P (timestamped, from investor terminal), shares S, latest EPS, consensus next-year net income.
1. Market cap = P × S. Sanity-check against a quoted market cap.
2. Trailing PE = P / EPS_ttm.
3. Forward EPS = consensus_next_year_NI / S; Forward PE = P / forward EPS.
4. Forward PEG = forward PE / growth%.
5. Compare P to consensus average target → premium/discount. Note if at/above the high estimate (priced for the bull case) or if targets look stale in a fast move.
6. Noise-robust takeaway: a conclusion that holds across every price/target version you have.
7. Disconfirmation: list what would break the thesis and what to monitor (next pre-announcement, capacity ramp, input bottlenecks, target revisions).
