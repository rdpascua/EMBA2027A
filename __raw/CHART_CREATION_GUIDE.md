# Growth Performance Analysis - Chart Creation Guide

## Files Created

I've created three CSV files optimized for analyzing Growth Performance and Competitive Standing:

1. **growth_performance_data.csv** - Core metrics for latest year
2. **growth_comparison_by_year.csv** - Year-over-year comparison
3. **growth_rankings.csv** - Competitive positioning analysis

## Recommended Chart Approach for Competitive Analysis

### 1. **Clustered Bar Chart - Overall Growth Comparison**
**Purpose:** Show all airlines side-by-side across growth metrics

**Data Source:** `growth_performance_data.csv`

**Steps in Excel:**
- Open the CSV file
- Select data range (A1:D7)
- Insert → Charts → Clustered Column Chart
- This shows all three growth metrics for each airline

**Insight:** Quickly identify which airlines are growing vs. declining

---

### 2. **Individual Metric Charts - Competitive Ranking**
**Purpose:** Focus on one metric at a time to see clear winners/losers

**For Sales Growth:**
- Select columns A and B from `growth_performance_data.csv`
- Insert → Bar Chart (horizontal bars work well for rankings)
- Sort by value to show ranking

**For Operating Income Growth:**
- Select columns A and C
- Create separate chart

**For Net Income Growth:**
- Select columns A and D
- Create separate chart

**Insight:** Clear competitive hierarchy in each metric

---

### 3. **Stacked/Grouped Chart - Multi-Year Trend**
**Purpose:** Show how competitive positions changed over time

**Data Source:** `growth_comparison_by_year.csv`

**Steps:**
- Select all data (A1:H7 for each metric group)
- Create clustered column chart
- Group by airline with year comparison

**Insight:** Which airlines improved/declined over time

---

### 4. **Scatter Plot - Quadrant Analysis**
**Purpose:** Map competitive positioning across two dimensions

**Recommended Combinations:**
- X-axis: Sales Growth
- Y-axis: Operating Income Growth
- OR
- X-axis: Sales Growth
- Y-axis: Net Income Growth

**Steps:**
- Use data from `growth_performance_data.csv`
- Insert → Scatter Chart
- Add quadrant lines at 0% or median values
- Label each point with airline name

**Quadrants:**
- Top Right: Strong performers (growing sales + income)
- Bottom Right: Revenue growth but profit challenges
- Top Left: Profit growth despite sales challenges
- Bottom Left: Struggling on both fronts

**Insight:** Strategic positioning and performance clusters

---

### 5. **Heatmap/Conditional Formatting**
**Purpose:** Visual color-coding of performance

**Steps:**
- Open `growth_rankings.csv` or `growth_performance_data.csv`
- Select the metric columns (B2:D7)
- Home → Conditional Formatting → Color Scales
- Use Red-Yellow-Green scale

**Insight:** Instant visual identification of strong/weak areas

---

## Key Insights from the Data

### Best Overall Performer: **WestJet Airlines**
- #1 in Sales Growth (18.5%)
- #2 in Operating Income Growth (-2.3%)
- #1 in Net Income Growth (-7.8%)
- Most balanced growth profile

### Notable Outlier: **Lufthansa**
- Extreme Operating Income Growth (2753.3%) - likely recovery from previous loss
- Moderate sales growth (11.1%)
- Net income still declining (-63.8%)

### Struggling Airlines: **Continental & Air Canada**
- Both showing significant declines across all metrics
- Likely impacted by 2008 financial crisis

### Growth Leaders: **WestJet & Southwest**
- Positive sales growth in difficult market
- Better positioned than competitors

## Recommended Chart Layout in Excel

**Dashboard Approach:**

**Sheet 1: Executive Summary**
- One large clustered column chart showing all metrics
- Conditional formatting table
- Key insights text box

**Sheet 2: Sales Growth Deep Dive**
- Horizontal bar chart (sorted)
- Year-over-year comparison
- Trend analysis

**Sheet 3: Profitability Focus**
- Operating Income chart
- Net Income chart
- Combined scatter plot

**Sheet 4: Competitive Positioning**
- Quadrant analysis scatter plot
- Rankings table from `growth_rankings.csv`

## Tips for Effective Visualization

1. **Color Consistency:** Use same color for each airline across all charts
2. **Sort Strategically:** Arrange by performance (best to worst) for clarity
3. **Add Data Labels:** Show exact percentages on bars
4. **Use Reference Lines:** Add 0% line to show positive vs negative growth
5. **Highlight Outliers:** Call attention to extreme values (like Lufthansa's 2753%)

## Quick Start in Excel

1. Open `growth_performance_data.csv` in Excel
2. Select cells A1:D7
3. Click Insert → Recommended Charts
4. Choose "Clustered Column"
5. Customize with chart title: "Airline Growth Performance Comparison"
6. Done! You have your first competitive analysis chart.
