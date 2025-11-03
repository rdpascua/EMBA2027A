# WestJet Investment Analysis Framework

---

## 1. WestJet's Performance & Financial Health

### **Purpose:**
Evaluate WestJet's standalone financial strength before comparing to competitors. Understand if the company is healthy or distressed.

---

### **Internal Signals: Company-Specific Performance**

Internal signals are metrics generated from WestJet's own financial statements. These show what is happening inside the company regardless of external conditions.

---

### **External Context: Industry and Economic Environment**

External context explains the environment in which WestJet operates. These are factors outside management's control that affect performance.

**Data Source:** Case text (pages 1-4), industry data from Exhibit 9

**Key External Factors (2008-2009):**

**1. Global Financial Crisis (2008)**
- Worst economic downturn since Great Depression
- Credit markets frozen, unemployment rising
- Consumer spending collapsing
- Business travel declining sharply

**Impact on Airlines:**
- IATA forecast: Industry loss of $9 billion in 2009 (double March 2009 estimates)
- Industry revenues falling from $528B (2008) to $448B (2009)
- Demand destruction across all regions

**2. Regional Airline Performance (2009 IATA Estimates):**
- Asia Pacific: -$3.3B loss (hardest hit, capacity-demand mismatch)
- Europe: -$1.8B loss (premium traffic collapse)
- North America: -$1.0B loss (early capacity cuts helped)
- Middle East: -$1.5B loss (hub vulnerability)
- Latin America: -$900M loss
- Africa: -$500M loss

**3. Fuel Price Volatility**
- Oil spiked to $147/barrel (July 2008)
- Crashed to $40/barrel (December 2008)
- Extreme volatility destroyed hedging strategies
- Airlines with locked-in high prices suffered most

**4. Credit Market Freeze**
- Aircraft financing unavailable
- Banks refusing to lend to airlines
- Airlines unable to refinance maturing debt
- Chapter 11 bankruptcies increasing (US)

**5. Competitive Dynamics**
- Legacy carriers (Continental, Air Canada) in distress
- Consolidation pressure increasing
- Capacity cuts industry-wide
- Fare wars as airlines fight for survival

**What External Context Shows:**

**The Industry Environment in 2008-2009:**
- Worst crisis in airline history
- No airline immune to demand collapse
- Survival, not growth, is the goal
- Financial strength determines who lives

**WestJet's Context:**
- Operating in Canadian market (smaller, more stable than US)
- Not dependent on international long-haul (less exposed to global collapse)
- Point-to-point model (less complex than hub-and-spoke)
- Low-cost structure (better positioned for fare competition)

**Key Insight:**
Any profitability in 2008 is exceptional. WestJet's ability to grow revenue (18.5%) and maintain profit (C$178M net income) during industry collapse is remarkable. Context matters when evaluating performance.

**Comparison to External Environment:**

| Factor | Industry Condition | WestJet Performance |
|--------|-------------------|---------------------|
| Revenue | Falling globally | Growing 18.5% |
| Profitability | $9B industry loss forecast | C$178M profit |
| Capacity | Cutting flights | Adding capacity |
| Financing | Credit frozen | Generating cash, reducing debt |
| Stock prices | Collapsing 40-60% | Down 50% (in line with sector) |

**Interpretation:**
WestJet's fundamentals diverged positively from industry trends. Company outperformed operationally but stock price fell with the sector (contagion effect). This suggests market treated all airlines equally despite fundamental differences.

---

### **A. Profitability Trends (5-Year Analysis)**

**Data Source:** `westjet_5year_ratios_exhibit4.csv`

**Chart Type:** Line Chart with Multiple Series

**Setup:**
- X-axis: Years (2004, 2005, 2006, 2007, 2008)
- Y-axis: Percentage
- 4 Lines:
  - Operating Income Margin (blue)
  - Net Profit Margin (green)
  - Return on Equity (orange)
  - Revenue Growth (gray, dashed)

**How to Read:**
- **Upward trending lines** = improving profitability
- **Downward trending lines** = deteriorating profitability
- **Gap between operating and net margin** = impact of interest/taxes
- **ROE higher than margins** = leverage amplifying returns

**What It Shows:**
WestJet's profitability recovered from 2004 losses (-0.9% operating margin, -1.7% net margin) to peak in 2007 (13.9% operating, 9.0% net, 20.3% ROE), then declined slightly in 2008 crisis (11.5% operating, 7.0% net, 16.4% ROE) but remained strongly profitable.

**Key Insight:**
The 2008 decline is modest compared to industry collapse. WestJet maintained double-digit operating margins while competitors went negative. This suggests structural resilience, not temporary luck.

---

### **B. Leverage & Debt Coverage**

**Data Source:** `westjet_5year_ratios_exhibit4.csv` + `balance_sheets_exhibit1.csv`

**Chart Type:** Combination Chart (Column + Line)

**Setup:**
- Primary Y-axis (left): Debt to Assets % (columns)
- Secondary Y-axis (right): Interest Coverage Ratio (line with markers)
- X-axis: Years (2004-2008)

**How to Read:**
- **Debt to Assets:** Lower is safer (less debt relative to assets)
- **Interest Coverage:** Higher is safer (more earnings to cover interest)
- Rule of thumb: Interest coverage above 3.0x = comfortable, below 1.5x = distress

**What It Shows:**
WestJet reduced debt from 53.5% of assets (2004) to 41.3% (2008). Interest coverage improved from near-bankruptcy levels (1.1x in 2005) to healthy 5.7x (2008). Company deleveraged while growing.

**Key Insight:**
WestJet has been actively strengthening its balance sheet. Lower debt + higher coverage = more financial flexibility during crisis. Opposite of Continental/Air Canada which increased leverage into the crisis.

---

### **C. Operating Efficiency Metrics**

**Data Source:** `westjet_5year_ratios_exhibit4.csv`

**Chart Type:** Grouped Column Chart

**Setup:**
- X-axis: Years (2004-2008)
- Y-axis: Days
- 3 bar series per year:
  - Days Receivables (how fast customers pay)
  - Days Inventory (how fast inventory turns)
  - Days Payables (how long WestJet takes to pay suppliers)

**How to Read:**
- **Days Receivables:** Lower is better (collecting cash faster)
- **Days Inventory:** Lower is better (efficient inventory management)
- **Days Payables:** Higher can be better (using supplier credit) but too high = strained relationships
- **Cash conversion cycle** = Receivables + Inventory - Payables (lower is better)

**What It Shows:**
WestJet has extremely efficient working capital:
- Receivables: 2.4 days (near-instant cash collection, typical for airlines selling tickets upfront)
- Inventory: 2.9 days (minimal parts inventory, lean operations)
- Payables: 42.9 days (using supplier credit effectively)

**Key Insight:**
WestJet collects cash almost immediately (ticket sales) but pays suppliers 43 days later. This negative cash conversion cycle means operations generate cash rather than consume it. This is a huge competitive advantage.

---

### **D. Revenue Growth vs Profit Growth**

**Data Source:** `income_statements_exhibit2.csv` + `westjet_5year_ratios_exhibit4.csv`

**Chart Type:** Waterfall Chart or Stacked Column

**Setup:**
Show 2008 vs 2007 comparison:
- Revenue growth: +18.5%
- Operating expense growth: +23.0%
- Operating income growth: -2.3%
- Net income growth: -7.8%

**How to Read:**
Compare the relative size of each bar:
- If revenue growth > expense growth = margin expansion (good)
- If expense growth > revenue growth = margin compression (bad but may be strategic)
- If profit growth < revenue growth = profitability under pressure

**What It Shows:**
WestJet grew revenue 18.5% but expenses grew faster (23.0%), causing profit to decline slightly. This suggests:
- Investment phase (adding capacity)
- Cost pressures (fuel, labor)
- Short-term margin compression for long-term market share

**Key Insight:**
Despite margin compression, WestJet still achieved 11.5% operating margin and 7.0% net margin. Competitors with similar expense growth went into losses. WestJet's base efficiency is so high it can absorb cost inflation better than peers.

---

### **E. Common-Sized Income Statement (2007 vs 2008)**

**Data Source:** `common_sized_income_statements_exhibit6.csv`

**Chart Type:** 100% Stacked Column (Side by Side)

**Setup:**
Two columns (2007 and 2008), each showing breakdown:
- Operating Expenses: 80.1% (2007), 83.2% (2008)
- Depreciation: 5.9% (2007), 5.3% (2008)
- Operating Income: 13.9% (2007), 11.5% (2008)
- Interest: 2.4% (2007), 2.0% (2008)
- Tax: 2.1% (2007), 3.0% (2008)
- Net Income: 9.0% (2007), 7.0% (2008)

**How to Read:**
Each column adds to 100% (representing total revenue). Compare the size of each segment year over year. Expanding segments are consuming more of each revenue dollar. Shrinking segments are becoming more efficient.

**What It Shows:**
Operating expenses grew from 80.1% to 83.2% of revenue (3.1 percentage point margin compression). This came mostly from operating costs, not interest or taxes. Net margin compressed from 9.0% to 7.0%.

**Key Insight:**
Margin compression is real but controlled. WestJet went from excellent (9.0% net margin) to very good (7.0% net margin). Competitors went from mediocre to disaster. The starting point matters.

---

### **F. Cash Flow Analysis**

**Data Source:** `cash_flow_statements_exhibit3.csv`

**Chart Type:** Grouped Column Chart (Positive/Negative)

**Setup:**
- X-axis: Cash flow categories
- Y-axis: Millions (allow negative values)
- 2 bars per category (2007 and 2008):
  - Operating Cash Flow
  - Investing Cash Flow
  - Financing Cash Flow
  - Net Change in Cash

**How to Read:**
- **Operating CF:** Should be positive and large (core business generates cash)
- **Investing CF:** Typically negative (buying planes, equipment)
- **Financing CF:** Can be positive (raising money) or negative (paying debt, dividends)
- **Net Change:** Positive = building cash, negative = burning cash

**What It Shows:**
2008 WestJet:
- Operating CF: C$460M (strong cash generation)
- Investing CF: -C$200M (modest capital spending)
- Financing CF: -C$115M (paying down debt)
- Net Change: +C$145M (building cash reserves)

2007 WestJet:
- Operating CF: C$541M (even stronger)
- Investing CF: -C$200M (similar capex)
- Financing CF: -C$60M (debt payments)
- Net Change: +C$281M (big cash build)

**Key Insight:**
WestJet generates positive free cash flow (operating cash exceeds capital spending). Company is self-funding and reducing debt. This is rare in airlines, which typically burn cash and raise debt. Strong cash generation provides cushion for crisis.

---

### **Summary: Internal Signals vs External Context**

**The Complete Picture:**

| Dimension | Internal Signal (What WestJet Controls) | External Context (Industry/Economy) | WestJet's Position |
|-----------|----------------------------------------|-------------------------------------|-------------------|
| **Profitability** | Operating margin 11.5%, net margin 7.0% | Industry facing $9B loss in 2009 | Best-in-class margins while industry bleeds |
| **Growth** | Revenue +18.5%, adding capacity | Industry cutting capacity, revenue falling | Counter-cyclical expansion |
| **Leverage** | Debt/Assets 41.3%, coverage 5.7x | Credit markets frozen, financing unavailable | Deleveraging, self-funding |
| **Cash Flow** | Operating CF C$460M, free CF positive | Airlines burning cash, raising debt | Generating cash, building reserves |
| **Efficiency** | Days receivables 2.4, inventory 2.9 | Industry average 10-15 days | Fastest cash collection cycle |
| **Resilience** | Net income -7.8% decline | Competitors -44% to -339% decline | Minimal profit erosion |

**Key Insights:**

**1. Absolute Performance (Internal):**
WestJet is profitable, growing, and generating cash. By any standard, these are strong results.

**2. Relative Performance (vs External Context):**
WestJet is doing the impossible. Growing and profitable during worst airline crisis in history. This is exceptional.

**3. The Divergence:**
Internal signals are excellent. External context is catastrophic. WestJet insulated itself from industry collapse. This is the definition of competitive advantage.

**4. The Valuation Question:**
If fundamentals are this strong, why is stock down 50%? Three possibilities:
- Market irrationally lumping WestJet with failing airlines (opportunity)
- Market sees future deterioration not yet visible in financials (warning)
- Stock priced for perfection in 2007, now repricing to reality (fair value)

**What Charts to Create for Section 1:**

**Chart Set 1: Internal Signals (Time Series)**
- 5-year profitability trends (margins, ROE)
- 5-year leverage trends (debt/assets, coverage)
- 5-year efficiency trends (working capital metrics)
- 2-year cash flow comparison (2007 vs 2008)

**Chart Set 2: External Context (Comparative)**
- Industry revenue forecast (2008 actual vs 2009 forecast)
- Regional loss estimates (bar chart, 2009)
- WestJet vs industry performance (table format)

**Chart Set 3: Internal vs External (Divergence)**
- WestJet growth vs industry decline (diverging lines)
- WestJet profitability vs peer losses (waterfall)
- Cash generation vs industry cash burn (columns)

**The Story These Charts Tell:**

**Act 1:** WestJet recovered from 2004-2005 struggles to become highly profitable by 2007.

**Act 2:** 2008 crisis hit. Industry collapsed. WestJet's margins compressed slightly but remained profitable.

**Act 3:** While competitors hemorrhaged cash and faced bankruptcy, WestJet generated cash and reduced debt.

**The Punchline:** WestJet's internal performance diverged massively from external environment. Company demonstrated structural resilience, not cyclical luck. This is the foundation for the investment thesis.

---

## 2. Competitive Standing

---

## 2A. Profitability vs Peers

**Data Source:** `profitability_multiaxis_filtered.csv` (already created)

**Chart Type:** Combination Chart (Clustered Column + Line with Secondary Axis)

**Setup:**
- Primary Y-axis (left, 0-20%): ROE and ROA as columns
- Secondary Y-axis (right, 0-12%): Operating Margin and Net Profit Margin as lines
- X-axis: Airlines (WestJet, Southwest, Lufthansa, Singapore)
- Exclude Continental and Air Canada (extreme negatives break scale)

**How to Read:**
**Return Metrics (Columns):**
- ROE (Return on Equity): Profit generated per dollar of shareholder money. Higher = better shareholder returns. Above 15% is excellent, 10-15% is good, below 10% is mediocre.
- ROA (Return on Assets): Profit generated per dollar of all assets. Higher = better asset utilization. Above 5% is good for airlines, 3-5% is acceptable, below 3% is poor.

**Margin Metrics (Lines):**
- Operating Margin: Operating profit as % of revenue. Shows operational efficiency before financing costs. Above 10% is excellent for airlines, 5-10% is good, below 5% is struggling.
- Net Profit Margin: Bottom-line profit as % of revenue. Shows total profitability after all costs. Above 7% is excellent for airlines, 3-7% is good, below 3% is marginal.

**What It Shows:**
WestJet dominates all four metrics:
- ROE: 16.4% (nearest competitor: Lufthansa 8.7%, 88% higher)
- ROA: 5.4% (nearest competitor: Singapore 4.6%, 17% higher)
- Operating Margin: 11.5% (nearest competitor: Singapore 5.6%, 2x higher)
- Net Profit Margin: 7.0% (tied with Singapore 7.2%)

**Key Insight:**
WestJet achieves premium airline margins (matching Singapore) with low-cost carrier capital efficiency (best ROE/ROA). This combination is extremely rare. Most airlines either have good margins with poor returns (Singapore, Lufthansa) or poor margins with decent returns (Southwest). WestJet has both.

**Why This Matters:**
High margins can be achieved by raising prices (Singapore premium model). High returns can be achieved by cutting costs and assets to the bone (Southwest model). Doing both simultaneously means WestJet has pricing power AND operational efficiency. This is a sustainable competitive advantage, not a temporary condition.

---

## 2B. Asset Efficiency

**Data Source:** `comparative_financial_ratios_exhibit10.csv`

**Chart Type:** Horizontal Bar Chart (for rankings)

**Setup:**
Create 4 separate charts showing competitive rankings:

**Chart 1: Total Asset Turnover**
- Y-axis: Airlines (ranked high to low)
- X-axis: Asset Turnover Ratio (Revenue / Total Assets)
- Formula meaning: How many dollars of revenue generated per dollar of assets
- Higher is better (more revenue per dollar of assets)

Rankings 2008:
1. Continental: 1.2x
2. Lufthansa: 1.1x
3. Air Canada: 0.9x
4. WestJet: 0.8x
5. Southwest: 0.8x
6. Singapore: 0.6x

**Chart 2: Days Receivables**
- Y-axis: Airlines
- X-axis: Days (lower is better)
- Measures: How long it takes to collect payment from customers

Rankings 2008 (lower is better):
1. WestJet: 2.4 days
2. Southwest: 6.9 days
3. Continental: 10.8 days
4. Air Canada: 25.1 days
5. Singapore: 33.9 days
6. Lufthansa: 44.1 days

**Chart 3: Days of Inventory**
- Y-axis: Airlines
- X-axis: Days (lower is better)
- Measures: How efficiently airline manages spare parts inventory

Rankings 2008 (lower is better):
1. WestJet: 2.9 days
2. Air Canada: 3.7 days
3. Continental: 5.7 days
4. Southwest: 7.4 days
5. Lufthansa: 9.1 days
6. Singapore: 13.7 days

**Chart 4: PP&E as % of Assets**
- Y-axis: Airlines
- X-axis: Percentage
- Formula: Net Plant, Property, Equipment / Total Assets
- From `common_sized_balance_sheets_exhibit5.csv`
- Lower can indicate newer fleet (less accumulated depreciation) or more capital-light model

Rankings 2008:
1. Southwest: 77.2% (most asset-heavy)
2. WestJet: 69.6%
3. Air Canada: 65.7%
4. Singapore: 55.5%
5. Continental: 57.8%
6. Lufthansa: 50.7% (most capital-light)

**How to Read These Together:**

**Asset Turnover Paradox:**
WestJet has lower asset turnover (0.8x) than Continental (1.2x) or Lufthansa (1.1x), but higher ROA (5.4% vs 2.7%). How is this possible?

Answer: Profitability matters more than turnover.
- Continental: High turnover, negative profit = ROA of -4.6%
- WestJet: Lower turnover, high profit margin = ROA of 5.4%

Formula: ROA = Asset Turnover × Profit Margin
- Continental: 1.2x turnover × -3.8% margin = -4.6% ROA
- WestJet: 0.8x turnover × 7.0% margin = 5.6% ROA (slight rounding difference from direct calculation)

**Working Capital Efficiency:**
WestJet collects cash in 2.4 days (fastest in industry). This is because:
- Most tickets sold online with immediate payment
- Corporate contracts settled quickly
- Minimal credit extended to customers

Compare to Lufthansa (44.1 days) which has:
- More complex corporate contracts
- International receivables with slower collection
- Cargo business with 30-60 day payment terms

**Inventory Efficiency:**
WestJet turns inventory every 2.9 days (near best). This means:
- Minimal spare parts on hand
- Just-in-time inventory management
- Lower capital tied up in warehouses

Singapore (13.7 days) has more inventory because:
- Larger fleet requires more spare parts
- International operations require distributed inventory
- Premium service requires more consumables (amenities, meals)

**Key Insight:**
Asset efficiency is not about single metrics. WestJet has:
- Lower asset turnover than peers (0.8x) BUT
- Fastest cash collection (2.4 days) AND
- Leanest inventory (2.9 days) AND
- Highest margins (7.0% net) AND
- Best returns (5.4% ROA)

This combination means WestJet extracts maximum profit from moderate asset levels. It is not trying to be Continental (high turnover, no profit) or Singapore (low turnover, high capital). WestJet found the sweet spot of balanced efficiency with high profitability.

---

## 2C. Growth Performance

**Data Source:** `growth_performance_data.csv` (already created)

**Chart Type:** Clustered Column Chart (what we already made)

**Review of What Chart Shows:**

**Sales Growth (Blue Bars):**
WestJet: 18.5% (tallest bar)
- Growing revenue faster than all competitors
- Gaining market share
- Adding capacity, routes, or passengers

Interpretation:
- 18.5% growth in a crisis year (2008) is exceptional
- Competitors ranged from 0.1% (Singapore) to 11.8% (Southwest)
- WestJet grew 57% faster than second-place Southwest

**Operating Income Growth (Orange Bars):**
WestJet: -2.3% (least negative, excluding Lufthansa outlier)
- Operating profit declined slightly but remained positive
- All peers except Lufthansa declined worse

Interpretation:
- Southwest: -43.2% (18x worse decline)
- Continental: -145.7% (from profit to massive loss)
- Air Canada: -133.1% (from profit to loss)
- Singapore: -57.5% (major profit erosion)
- Lufthansa: +2753% (outlier, recovery from near-zero 2007)

WestJet lost only 2.3% of operating profit despite 18.5% revenue growth and rising costs. This suggests pricing power or cost control kept margins nearly flat.

**Net Income Growth (Green Bars):**
WestJet: -7.8% (third best)
- Bottom-line profit declined but remained strongly positive
- Only Singapore (-44.0%) and Lufthansa (-63.8%) had comparable resilience

Interpretation:
- Southwest: -72.4% (profit collapsed)
- Continental: -227.5% (from profit to huge loss)
- Air Canada: -338.9% (from profit to catastrophic loss)

**Key Insight:**
WestJet's growth profile is ideal:
- Revenue UP (18.5%) = market share gains
- Profit DOWN slightly (-2.3% operating, -7.8% net) = resilience in crisis
- Gap between revenue growth and profit decline is minimal = structural efficiency

Contrast with Southwest:
- Revenue UP (11.8%) = also gaining share
- Operating profit DOWN (-43.2%) = margin collapse
- Net profit DOWN (-72.4%) = severe profitability erosion

WestJet grew 57% faster than Southwest but protected profits 6-10x better. This is the definition of quality growth.

**Alternative View: Growth Resilience Score**

Create a simple table showing:

| Airline | Revenue Growth | Operating Income Growth | Net Income Growth | Resilience Score |
|---------|----------------|-------------------------|-------------------|------------------|
| WestJet | +18.5% | -2.3% | -7.8% | Excellent |
| Southwest | +11.8% | -43.2% | -72.4% | Poor |
| Lufthansa | +11.1% | +2753%* | -63.8% | N/A |
| Continental | +7.1% | -145.7% | -227.5% | Catastrophic |
| Air Canada | +3.5% | -133.1% | -338.9% | Catastrophic |
| Singapore | +0.1% | -57.5% | -44.0% | Moderate |

*Outlier excluded

Resilience Score = How well did airline protect profits while growing revenue?
- Excellent: Profit decline < 10% while revenue growing double-digit
- Good: Profit decline 10-25%
- Poor: Profit decline > 40%
- Catastrophic: Profit became loss

---

## 2D. ROE Decomposition (DuPont Analysis)

**Data Source:** `comparative_financial_ratios_exhibit10.csv`

**Chart Type:** Waterfall Chart or Decomposition Tree

**Setup:**
Show how ROE is built from three components using DuPont formula:

ROE = Net Profit Margin × Asset Turnover × Equity Multiplier

Where:
- Net Profit Margin = Net Income / Revenue
- Asset Turnover = Revenue / Assets
- Equity Multiplier = Assets / Equity

**Create Comparison Table:**

| Component | WestJet | Southwest | Lufthansa | Singapore |
|-----------|---------|-----------|-----------|-----------|
| **Net Profit Margin** | 7.0% | 1.6% | 2.4% | 7.2% |
| **Asset Turnover** | 0.8x | 0.8x | 1.1x | 0.6x |
| **Equity Multiplier** | 3.0x | 2.9x | 3.2x | 1.7x |
| **= ROE** | 16.4% | 3.6% | 8.7% | 7.9% |

**Chart Approach:**
Create 4 separate waterfall charts, one per airline:

**WestJet Waterfall:**
```
Start: 0%
+ Net Profit Margin: 7.0%
× Asset Turnover: 0.8x = 5.6%
× Equity Multiplier: 3.0x = 16.4% (final ROE)
```

**How to Read DuPont Components:**

**Component 1: Net Profit Margin (7.0%)**
- Measures operational efficiency
- Every $1 of revenue yields $0.07 of profit
- High margin = pricing power or cost control
- WestJet: 7.0% (tied for best with Singapore 7.2%)
- Southwest: 1.6% (low, struggling with costs)

**Component 2: Asset Turnover (0.8x)**
- Measures asset utilization
- Every $1 of assets generates $0.80 of revenue
- Higher = more revenue from same assets
- WestJet: 0.8x (moderate)
- Lufthansa: 1.1x (highest, but with no margin)
- Singapore: 0.6x (lowest, capital-intensive)

**Component 3: Equity Multiplier (3.0x)**
- Measures financial leverage
- Assets = 3.0 × Equity
- Higher = more debt/leverage
- WestJet: 3.0x (moderate leverage)
- Singapore: 1.7x (low leverage, conservative)
- Lufthansa: 3.2x (high leverage)

**Interpretation by Airline:**

**WestJet (ROE 16.4%):**
- Excellent margin (7.0%) = operational winner
- Moderate turnover (0.8x) = balanced asset use
- Moderate leverage (3.0x) = amplifies good margins

Formula: 7.0% × 0.8 × 3.0 = 16.8% (approximately 16.4% with rounding)

**What makes WestJet special:** All three components are healthy. Not relying on extreme leverage (like Continental) or extreme turnover (like Lufthansa). Balanced model.

**Southwest (ROE 3.6%):**
- Poor margin (1.6%) = operational struggles
- Moderate turnover (0.8x) = similar asset efficiency to WestJet
- Moderate leverage (2.9x) = similar capital structure to WestJet

Formula: 1.6% × 0.8 × 2.9 = 3.7% (approximately 3.6%)

**Why Southwest fails:** The 1.6% margin is the killer. Southwest has similar asset efficiency and leverage to WestJet, but margins are 4.4x lower. This destroys ROE. Problem is operational, not financial.

**Lufthansa (ROE 8.7%):**
- Weak margin (2.4%) = operational inefficiency
- Good turnover (1.1x) = high asset utilization
- High leverage (3.2x) = using debt to boost returns

Formula: 2.4% × 1.1 × 3.2 = 8.4% (approximately 8.7%)

**Why Lufthansa is middle-tier:** Compensating for weak margins with high turnover and leverage. This is fragile. If margins compress further or debt costs rise, ROE collapses.

**Singapore (ROE 7.9%):**
- Excellent margin (7.2%) = premium pricing works
- Low turnover (0.6x) = capital-intensive model
- Low leverage (1.7x) = conservative financing

Formula: 7.2% × 0.6 × 1.7 = 7.3% (approximately 7.9%)

**Why Singapore underperforms:** Despite best-in-class margins (7.2%, tied with WestJet), the low asset turnover (0.6x) and conservative leverage (1.7x) limit ROE. Singapore chooses quality over returns. Invests heavily in premium product (low turnover) and avoids debt (low leverage).

**Key Insight - The WestJet Advantage:**

WestJet achieves 16.4% ROE by being excellent at margins (7.0%, tied for best) and balanced on turnover (0.8x) and leverage (3.0x).

Compare to peers:
- Southwest has same turnover and leverage but 4.4x lower margins = ROE collapses
- Singapore has same margins but lower turnover and leverage = ROE cut in half
- Lufthansa compensates for weak margins with high turnover/leverage = fragile ROE

**Visual Chart Recommendation:**
Create a stacked bar chart showing contribution to ROE:

X-axis: Airlines
Y-axis: ROE (0-18%)
Each bar divided into three segments showing contribution from:
- Margin (largest for WestJet and Singapore)
- Turnover (multiplier effect)
- Leverage (amplification effect)

This visually shows WestJet's balanced superiority vs peers' lopsided models.

---

## 3. Valuation Signals

---

## 3A. Price-to-Earnings (P/E) Ratio

**Data Source:** `valuation_metrics_exhibit9.csv`

**Chart Type:** Horizontal Bar Chart

**Setup:**
- Y-axis: Airlines (ranked by P/E)
- X-axis: P/E Ratio (Earnings Per Share / Stock Price)
- 2008 data only (2007 included for reference)

**Rankings 2008:**
1. Southwest: 35.7x (highest, most expensive)
2. WestJet: 9.4x
3. Singapore: 4.8x
4. Lufthansa: 4.3x
5. Continental: N/A (negative earnings, no P/E)
6. Air Canada: N/A (negative earnings, no P/E)

**How to Read P/E Ratio:**

**Basic Interpretation:**
P/E = Price / Earnings = How much investors pay for $1 of annual profit

Example: WestJet P/E of 9.4x means:
- Stock price = 9.4 × annual earnings per share
- If WestJet earns $1.39 per share (2008), stock should trade around $13.07
- Actual year-end price: C$13.12 (matches P/E)

**Valuation Ranges:**
- P/E < 10: Cheap/undervalued (or distressed)
- P/E 10-15: Fair value
- P/E 15-20: Moderately expensive
- P/E > 20: Expensive (or high growth expectations)

**What P/E Shows:**

**Southwest (P/E 35.7x):**
Market paying $35.70 for every $1 of earnings. Why so expensive?
- Brand strength (most trusted US airline)
- Consistency (36 years profitable)
- Market leader status
- BUT: Earnings quality is weak ($0.24 EPS in 2008, down from $0.84 in 2007)

Implication: Market is either:
1. Overvaluing Southwest based on past performance
2. Expecting rapid earnings recovery
3. Ignoring current weak profitability

**WestJet (P/E 9.4x):**
Market paying only $9.40 for every $1 of earnings. Why so cheap?
- Smaller size (less liquidity for investors)
- Canadian market (less visibility)
- Perceived risk (lumped with struggling airline sector)
- BUT: Earnings quality is highest (C$1.39 EPS, only slight decline from C$1.48 in 2007)

Implication: Market is undervaluing WestJet despite:
- Best profitability metrics (16.4% ROE)
- Best growth (18.5% revenue growth)
- Best resilience (minimal profit decline)

**Lufthansa (P/E 4.3x) and Singapore (P/E 4.8x):**
Market paying only $4-5 for every $1 of earnings. Why so cheap?
- European/Asian exposure to global crisis
- Large size = harder to adapt quickly
- Lower ROE (8.7% and 7.9%) = less efficient capital use

Implication: Market pricing in continued profitability weakness.

**The Valuation Anomaly:**

Create comparison table:

| Airline | P/E Ratio | ROE | Net Margin | Implied Market View |
|---------|-----------|-----|------------|---------------------|
| Southwest | 35.7x | 3.6% | 1.6% | Expensive despite weak fundamentals |
| WestJet | 9.4x | 16.4% | 7.0% | Cheap despite best fundamentals |
| Singapore | 4.8x | 7.9% | 7.2% | Very cheap, moderate fundamentals |
| Lufthansa | 4.3x | 8.7% | 2.4% | Very cheap, moderate fundamentals |

**Key Insight:**
WestJet has best profitability (ROE 16.4%, margin 7.0%) but second-lowest valuation (P/E 9.4x). Southwest has worst profitability (ROE 3.6%, margin 1.6%) but highest valuation (P/E 35.7x).

This disconnect suggests:
1. Market inefficiency (WestJet undervalued)
2. Market sees risks in WestJet not visible in 2008 data
3. Market overvalues brand/size (Southwest) vs fundamentals (WestJet)

---

## 3B. Market-to-Book Ratio

**Data Source:** `valuation_metrics_exhibit9.csv`

**Chart Type:** Scatter Plot

**Setup:**
- X-axis: Book Value per Share (Equity / Shares)
- Y-axis: Market Price per Share
- Diagonal line: Market = Book (M/B = 1.0)
- Points above line: Trading above book value (M/B > 1.0)
- Points below line: Trading below book value (M/B < 1.0)

**Calculate Book Value per Share:**

From data:
- WestJet: Book equity C$1,086M / 128M shares = C$8.48 per share
- Market price: C$13.12 (year-end 2008)
- M/B ratio: 13.12 / 8.48 = 1.55x (or use provided 1.9x for Aug 2009)

**Rankings 2008:**
1. WestJet: 1.9 (market values at 1.9x book equity)
2. Southwest: 1.3
3. Lufthansa: 0.5
4. Singapore: 0.7
5. Continental: 8.3 (meaningless, tiny book value from losses)
6. Air Canada: 1.1

**How to Read Market-to-Book:**

**M/B > 1.0:** Market believes company's assets worth more than book value
- Company generates returns above cost of capital
- Intangible value (brand, routes, customer loyalty)
- Growth potential

**M/B = 1.0:** Market price equals book value
- Company generating exactly cost of capital
- No premium for competitive advantage
- Fair value

**M/B < 1.0:** Market believes company's assets worth less than book value
- Company destroying value (earning below cost of capital)
- Assets impaired (planes worth less than stated)
- Distress situation

**Interpretation:**

**WestJet (M/B 1.9x):**
Market values WestJet at 1.9x its book equity. Why?
- High ROE (16.4%) justifies premium (ROE far exceeds cost of equity ~8-10%)
- Brand value and customer loyalty
- Route network and slots have intangible value
- Growth potential

Theory: If ROE = 16.4% and cost of equity = 10%, excess return = 6.4%. This justifies M/B premium.

**Southwest (M/B 1.3x):**
Lower premium than WestJet despite higher P/E (35.7x). Why?
- ROE only 3.6% (barely above cost of equity)
- Weak 2008 earnings justify lower book multiple
- Market values brand (high P/E) but not asset base (low M/B)

**Lufthansa (M/B 0.5x) and Singapore (M/B 0.7x):**
Trading below book value. Market says:
- Assets worth less than stated on balance sheet
- Planes, routes, brand impaired by crisis
- ROE (8.7% and 7.9%) does not justify book value
- Expect asset write-downs

**Key Insight - The Valuation Matrix:**

Create 2×2 matrix:

|  | High P/E (>15x) | Low P/E (<10x) |
|---|---|---|
| **High M/B (>1.5x)** | (empty) | **WestJet (P/E 9.4x, M/B 1.9x)** |
| **Low M/B (<1.5x)** | **Southwest (P/E 35.7x, M/B 1.3x)** | Lufthansa, Singapore |

**WestJet occupies the rare "High M/B, Low P/E" quadrant:**
- High M/B (1.9x) = Market recognizes high ROE and value creation
- Low P/E (9.4x) = Market undervalues current earnings

This is the "quality company at value price" sweet spot.

**Southwest occupies the opposite "Low M/B, High P/E" quadrant:**
- High P/E (35.7x) = Market overvalues weak current earnings
- Low M/B (1.3x) = Market recognizes low ROE does not justify premium

This is the "expensive company with deteriorating fundamentals" red flag.

---

## 3C. Stock Price Trends

**Data Source:** Exhibits 7 & 8 (stock charts), `valuation_metrics_exhibit9.csv`

**Chart Analysis:** Line chart showing indexed stock performance (Aug 2004 = 100)

**Key Observations:**

**WestJet Stock Journey (Aug 2004 - Aug 2009):**

**Phase 1: Climb (2004-2007)**
- Started: ~100
- Peak: ~150 (2007)
- Gain: +50%
- Steady upward trend with volatility

**Phase 2: Collapse (2007-2009)**
- Peak: ~150 (late 2007)
- Trough: ~75 (early 2009)
- Decline: -50% from peak
- Sharp drop during financial crisis

**Phase 3: Partial Recovery (2009)**
- Trough: ~75
- Aug 2009: ~87
- Recovery: +16% from bottom
- Still 42% below 2007 peak

**Comparative Performance (Aug 2004 - Aug 2009):**

Indexed to 100:
- S&P 500: ~100 (flat, 5-year return ≈ 0%)
- WestJet: ~87 (-13% total return)
- Southwest: ~110 (+10% total return)
- Continental: ~60 (-40% total return)
- Air Canada: ~50 (-50% total return)
- Lufthansa: ~120 (+20% total return)
- Singapore: ~140 (+40% total return)

**How to Read Stock Performance:**

**WestJet vs Peers:**

**WestJet vs Southwest (most comparable):**
- Both low-cost carriers
- Both profitable in 2008
- Southwest stock: +10% over 5 years
- WestJet stock: -13% over 5 years
- Gap: 23 percentage points

Why the disconnect?
- WestJet fundamentals superior (ROE 16.4% vs 3.6%)
- WestJet growth superior (18.5% vs 11.8%)
- Yet Southwest stock outperformed
- Implication: Market undervaluing WestJet

**WestJet vs Singapore/Lufthansa:**
- Singapore: +40% over 5 years, ROE 7.9%
- Lufthansa: +20% over 5 years, ROE 8.7%
- WestJet: -13% over 5 years, ROE 16.4%

Why did inferior ROE airlines outperform?
- Size and liquidity (larger stocks, more institutional ownership)
- Geographic diversification perceived as safer
- WestJet seen as Canadian regional, not global player

**The August 2009 Valuation Question:**

Stock prices on Aug 14, 2009:
- WestJet: C$11.62 (down 50% from Dec 2007 peak of ~C$23)
- P/E ratio: 9.4x (using 2008 earnings)
- M/B ratio: 1.9x

**Bull Case (Buy):**
1. Fundamentals are best-in-class (ROE 16.4%, margin 7.0%)
2. Growth is highest (18.5% revenue growth)
3. Crisis resilience proven (minimal profit decline)
4. Stock down 50% despite strong performance = oversold
5. P/E of 9.4x is cheap for best profitability
6. M/B of 1.9x reflects quality but not excessive premium

**Bear Case (Sell):**
1. Stock has been declining for 2 years despite strong fundamentals
2. Market sees something financials don't show
3. Canadian market is smaller, limited growth runway
4. Competition from Air Canada recovery could intensify
5. 2008 was peak earnings, 2009-2010 will be worse
6. Fuel prices could spike again, eroding low-cost advantage

**Key Insight - The Disconnect:**

Create table showing fundamental performance vs stock performance:

| Metric | Rank (1=best) | Stock Performance Rank |
|--------|---------------|------------------------|
| ROE | 1st (16.4%) | 4th (-13% 5-year) |
| Net Margin | 1st (7.0%) | 4th |
| Revenue Growth | 1st (18.5%) | 4th |
| Op Income Resilience | 1st (-2.3%) | 4th |

WestJet ranks #1 in fundamentals but #4 in stock performance. This is the central puzzle.

**Possible Explanations:**

**1. Market Inefficiency**
- Small cap stock, less analyst coverage
- Canadian listing, less US investor attention
- Oversold during crisis, will recover

**2. Forward-Looking Concerns**
- 2008 was peak, deterioration ahead
- Competitive threats increasing
- Fuel/cost inflation will hit hardest

**3. Sector Contagion**
- Entire airline sector sold off
- WestJet unfairly lumped with failing carriers
- Quality doesn't matter in panic selling

**4. Lack of Catalysts**
- No major growth announcements
- Modest dividend (not paying out much)
- Share buybacks limited

---

## Summary Framework: The Investment Decision

**The Three Lenses:**

**Lens 1: Fundamental Health (Sections 1 & 2)**
- Verdict: Excellent
- Best profitability, best growth, best resilience
- Clear competitive advantages

**Lens 2: Relative Valuation (Section 2A-2D)**
- Verdict: Best value in peer group
- Highest returns, lowest P/E (vs quality)
- Market undervaluing fundamentals

**Lens 3: Market Signals (Section 3)**
- Verdict: Concerning
- Stock down 50%, underperforming peers
- Disconnect between fundamentals and price

**The Decision:**

This analysis reveals a **fundamental-market disconnect**. WestJet has best operational performance but worst stock performance. This creates two possible investment theses:

**Contrarian Buy:** Market is wrong, fundamentals will eventually drive stock recovery. Current price is generational opportunity.

**Cautious Sell:** Market is right, something bad is coming that financials don't yet show. Preserve capital by selling before next drop.

**The case does not answer which view is correct. The analysis provides the framework. The investor must decide.**