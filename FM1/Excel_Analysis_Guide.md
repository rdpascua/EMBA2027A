# WhichKraft Excel Analysis Guide

## File: `WhichKraft_Analysis_Charts.xlsx`

This comprehensive Excel workbook contains 10 sheets covering all aspects of the case analysis, based strictly on the data from the case files.

---

## **Sheet Overview**

### **Sheet 1: Q1 2014 Actual Data**
**Purpose:** Baseline financial position

**Contains:**
- Complete Income Statement with Rs amounts and % of sales
- Complete Balance Sheet with Rs amounts and % of assets
- Key Metrics dashboard (burn rate, runway, breakeven)
- Bar Chart: Cost Structure vs Revenue

**Key Numbers:**
- Sales: Rs 141,350
- Gross Margin: 38.8%
- Net Loss: Rs 224,660
- Cash: Rs 628,195
- Runway: 2.8 quarters

---

### **Sheet 2: Sensitivity Analysis**
**Purpose:** Compare base case (28.7% COGS, 0-day AR) vs sensitivity (35% COGS, 70-day AR)

**Contains:**
- Assumption comparison table
- Impact analysis calculations
- Gross profit comparison
- Working capital requirements
- Bar Chart: Gross Margin Comparison
- Bar Chart: Working Capital Requirements

**Key Finding:**
- Sensitivity scenario results in Rs 117,338 worse cash position per quarter

---

### **Sheet 3: Forecast Template**
**Purpose:** Ready-to-use forecast model

**Contains:**
- Pre-loaded Q1 2014 actuals
- Formula-driven calculations for 2014-15, 2015-16, 2016-17
- Yellow highlighted cells = YOUR INPUT AREAS (sales, SG&A assumptions)
- Auto-calculates: COGS, Other Direct, Inventory, Cash

**How to Use:**
1. Enter sales assumptions in yellow cells (columns C, D, E)
2. Enter SG&A assumptions in yellow cells
3. All other items calculate automatically
4. Cash formula: Beginning Cash + Net Income - Inventory Change

---

### **Sheet 4: Summary & Recommendations**
**Purpose:** Executive summary of findings

**Contains:**
- Key findings from Q1 2014
- Sensitivity analysis impact summary
- Strategic recommendations (modify strategy)
- Action timeline (Month 1-18)

---

### **Sheet 5: Common-Sized Statements**
**Purpose:** Percentage analysis for easier comparison (addresses case requirement)

**Contains:**
- Common-sized Income Statement (all items as % of sales)
- Common-sized Balance Sheet (all items as % of total assets)
- Template for forecast periods

**Key Insight:**
- Shows SG&A at 197.8% of sales (critical problem)
- Cash represents 81% of assets

---

### **Sheet 6: Financial Ratios Analysis**
**Purpose:** Assess profitability, liquidity, and capital position (Question 4)

**Contains:**
- **Profitability Ratios:**
  - Gross Profit Margin: 38.8%
  - Operating Margin: -158.9%
  - ROA/ROE: -29.0%

- **Liquidity & Efficiency:**
  - Days Inventory: 54 days
  - Days Receivables: 0 days
  - Cash Conversion Cycle: 54 days
  - Asset Turnover: 0.73x (annualized)

- **Capital Structure:**
  - Debt-to-Equity: 0% (no debt)
  - Burn Rate: Rs 224,660/quarter
  - Cash Runway: 2.8 quarters

---

### **Sheet 7: Scenario Comparison**
**Purpose:** Side-by-side comparison of different scenarios

**Contains:**
- Scenario assumptions table
- Base Case vs Sensitivity vs Conservative scenarios
- Comparison metrics (revenue, gross profit, net income, cash, WC, ROE)
- Template for adding projected values

**Use For:**
- Comparing multiple forecast scenarios
- What-if analysis
- Presentation to stakeholders

---

### **Sheet 8: Funding Gap Analysis**
**Purpose:** Identify when external funding is needed (Question 6)

**Contains:**
- Cash flow projection table
- Funding gap calculation
- Triggers for external funding:
  1. Cash below Rs 100K
  2. Negative cash flow for 2 quarters
  3. Working capital > 50% of assets
  4. Revenue growth below projections
- Line Chart: Cash Runway Projection

**Conclusion:**
- Base case: Need Rs 500-750K within 6-9 months
- Sensitivity: Need Rs 1.5M+ within 3-6 months

---

### **Sheet 9: Breakeven Analysis**
**Purpose:** Calculate path to profitability (Question 4 & 7)

**Contains:**
- Breakeven calculation for Base vs Sensitivity
- Required sales growth multiples
- Path to profitability milestones:
  - Breakeven
  - 5% net margin
  - 10% net margin
- Time to breakeven at various growth rates
- Bar Chart: Breakeven Sales Required

**Key Finding:**
- Base: Need 5.1x sales growth to breakeven
- Sensitivity: Need 18.0x sales growth (unrealistic)

---

### **Sheet 10: Key Insights & Risks**
**Purpose:** Synthesize patterns and risks (Question 4 & 7)

**Contains:**

**Emerging Patterns:**
1. Cost structure pattern (SG&A dominates)
2. Margin pattern (decent gross margin)
3. Cash pattern (strong position depleting rapidly)
4. Capital pattern (22.5% equity burned in 3 months)
5. Working capital pattern (asset-light is positive)

**Risk Assessment:**
- **High Severity:** Cash runway, operating leverage, scale requirements
- **Medium Severity:** Market, execution, working capital (if sensitivity)
- **Low Severity:** Financial (no debt), liquidity (currently ok)

**Sustainability Assessment:**
- Current path: NOT SUSTAINABLE
- Base case path: POTENTIALLY SUSTAINABLE (with execution)
- Sensitivity path: NOT RECOMMENDED

---

## **How to Use This Workbook**

### **For Question 3 (Forecast):**
1. Go to **Sheet 3: Forecast Template**
2. Enter sales assumptions in yellow cells
3. Enter SG&A assumptions in yellow cells
4. Review calculated results
5. Copy key numbers to **Sheet 5** for common-sized analysis
6. Copy ratios to **Sheet 6** for ratio analysis

### **For Question 4 (Financial Health):**
1. Review **Sheet 6: Financial Ratios**
2. Check **Sheet 5: Common-Sized Statements**
3. Refer to **Sheet 10: Key Insights & Risks**
4. Use charts from Sheets 1 and 2

### **For Question 5 (Sensitivity):**
1. Use **Sheet 2: Sensitivity Analysis**
2. Compare with base case in **Sheet 1**
3. Update **Sheet 7: Scenario Comparison**
4. Use charts showing impact

### **For Question 6 (Funding):**
1. Review **Sheet 8: Funding Gap Analysis**
2. Update cash flow projections based on your forecast
3. Identify funding triggers
4. Use cash runway chart

### **For Question 7 (Recommendation):**
1. Synthesize findings from **Sheet 10**
2. Reference **Sheet 9: Breakeven Analysis**
3. Use **Sheet 4: Summary & Recommendations**
4. Support with charts from all sheets

---

## **Charts Available**

1. **Cost Structure vs Revenue** (Sheet 1) - Bar chart
2. **Gross Margin Comparison** (Sheet 2) - Bar chart
3. **Working Capital Requirements** (Sheet 2) - Bar chart
4. **Cash Runway Projection** (Sheet 8) - Line chart
5. **Breakeven Sales Required** (Sheet 9) - Bar chart

---

## **Key Numbers Reference (Q1 2014 Actual)**

| Category | Value |
|----------|-------|
| Net Sales | Rs 141,350 |
| COGS | Rs 40,623 (28.7%) |
| Other Direct | Rs 45,833 (32.4%) |
| Gross Profit | Rs 54,894 (38.8%) |
| SG&A | Rs 279,554 (197.8%) |
| Net Loss | Rs (224,660) |
| Cash | Rs 628,195 |
| Inventory | Rs 21,203 |
| Total Assets | Rs 775,340 |
| Paid Capital | Rs 1,000,000 |
| Total Equity | Rs 775,340 |

---

## **Critical Analysis Points**

### **The Core Problem:**
SG&A at Rs 279,554/quarter is 197.8% of sales (Rs 141,350)
- Industry norm: 20-40% of sales
- WhichKraft: Nearly 2x revenue

### **The Math:**
For every Rs 1 of sales:
- Generate: Rs 0.388 gross profit
- Spend: Rs 1.978 on SG&A
- Result: Rs 1.589 loss

### **Path to Viability:**
Need either:
1. 5x sales growth (to Rs 720K/quarter) while holding SG&A constant, OR
2. 40% SG&A cut (to Rs 180K) at current sales, OR
3. Combination of both

### **Sensitivity Scenario Problem:**
Reduces gross margin from 38.8% to 32.6%
- Breakeven moves from 5.1x to 18.0x current sales
- Makes business model unviable

---

## **Next Steps for Analysis**

1. **Determine sales assumptions** from case (need to find growth rates)
2. **Input forecasts** in Sheet 3
3. **Calculate ratios** in Sheet 6 based on forecasts
4. **Update charts** with forecast data
5. **Complete scenario comparison** in Sheet 7
6. **Finalize funding analysis** in Sheet 8
7. **Make final recommendation** based on all data

---

## **Notes**

- All data based strictly on case files (no external assumptions)
- Formulas are set up but need sales/SG&A inputs
- Yellow cells indicate required inputs
- Charts will update automatically when data is entered
- Common-sized statements help identify trends over time
- Ratio analysis addresses financial health question directly

---

**File Location:** `/Users/ricardopascua/Projects/aim/FM1/WhichKraft_Analysis_Charts.xlsx`

**Companion Document:** `WhichKraft_Financial_Analysis.md`
