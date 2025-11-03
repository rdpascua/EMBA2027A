# Asset Efficiency Bubble Chart - Setup Instructions

## **File to Use:**
`asset_efficiency_bubble_chart.csv`

---

## **Excel Setup Instructions:**

### **Step 1: Prepare the Data**

Open `asset_efficiency_bubble_chart.csv` in Excel

Your data should look like:
```
Airline          | Asset Growth % | ROA % | Revenue 2008 (Billions) | Status
WestJet          | 9.9           | 5.4   | 2.08                   | Profitable
Southwest        | -14.7         | 1.2   | 11.02                  | Profitable
Continental      | 4.8           | -4.6  | 15.24                  | Loss
Lufthansa        | 0.4           | 2.7   | 34.87                  | Profitable
Singapore        | -6.4          | 4.6   | 10.53                  | Profitable
Air Canada       | -4.0          | -9.0  | 8.35                   | Loss
```

---

### **Step 2: Create Bubble Chart**

1. Select columns B through D (Asset Growth %, ROA %, Revenue)
2. **Do NOT select** Airline names or Status column yet
3. Click **Insert** → **Charts** → **Scatter** → **Bubble**

Excel will create basic bubble chart with:
- X-axis: Asset Growth %
- Y-axis: ROA %
- Bubble size: Revenue

---

### **Step 3: Add Airline Labels**

**Method A: Manual Labels (Recommended)**
1. Right-click on each bubble
2. Select **Add Data Label**
3. Right-click the label → **Format Data Label**
4. Check **Value From Cells**
5. Select airline names from Column A
6. Uncheck all other options (X Value, Y Value, Bubble Size)

**Method B: Using Data Labels**
1. Click any bubble in the chart
2. Chart Design → Add Chart Element → Data Labels → More Options
3. In Format Data Labels pane:
   - Check "Value from Cells"
   - Select range A2:A7 (airline names)
   - Position: Center or Above

---

### **Step 4: Format Axes**

**X-Axis (Asset Growth %):**
- Right-click X-axis → Format Axis
- Set Minimum: -16
- Set Maximum: 12
- Set Major Unit: 4
- Add Axis Title: "Asset Growth 2007-2008 (%)"

**Y-Axis (ROA %):**
- Right-click Y-axis → Format Axis
- Set Minimum: -10
- Set Maximum: 6
- Set Major Unit: 2
- Add Axis Title: "Return on Assets (%)"

---

### **Step 5: Add Quadrant Lines**

**Add Vertical Line at X = 0:**
1. Chart Design → Add Chart Element → Lines → Drop Lines
2. OR manually: Insert → Shapes → Line
3. Draw vertical line at X = 0

**Add Horizontal Line at Y = 0:**
1. Insert → Shapes → Line
2. Draw horizontal line at Y = 0

**Format lines:**
- Style: Dashed
- Color: Gray
- Width: 1pt

---

### **Step 6: Color Code Bubbles**

**Separate into Two Series for Color:**

**Series 1: Profitable (Blue)**
- WestJet, Southwest, Lufthansa, Singapore

**Series 2: Loss-Making (Red)**
- Continental, Air Canada

**How to Split:**
1. Right-click chart → Select Data
2. Remove current series
3. Add Series 1: Select WestJet, Southwest, Lufthansa, Singapore rows
4. Add Series 2: Select Continental, Air Canada rows
5. Format each series with different colors

**Alternative (Easier):**
1. Click individual bubbles
2. Right-click → Format Data Point
3. Change fill color individually:
   - WestJet: Dark Blue
   - Southwest: Light Blue
   - Lufthansa: Green
   - Singapore: Teal
   - Continental: Red
   - Air Canada: Dark Red

---

### **Step 7: Add Chart Elements**

**Chart Title:**
"Asset Efficiency & Growth: WestJet vs Competitors (2008)"

**Subtitle (as text box):**
"Bubble size represents 2008 revenue (USD billions)"

**Legend:**
- Create custom legend with colored squares
- "● Blue = Profitable   ● Red = Loss"

**Gridlines:**
- Major gridlines for both axes
- Style: Light gray, thin

---

### **Step 8: Add Quadrant Labels**

Add 4 text boxes in each quadrant:

**Top-Right (High ROA + Growing Assets):**
"IDEAL POSITION
Growing & Profitable"

**Top-Left (High ROA + Shrinking Assets):**
"DEFENSIVE
Profitable but Shrinking"

**Bottom-Right (Low ROA + Growing Assets):**
"DANGER ZONE
Growing into Losses"

**Bottom-Left (Low ROA + Shrinking Assets):**
"DISTRESSED
Shrinking & Unprofitable"

Position these labels outside the data points, in corners of each quadrant.

---

### **Step 9: Highlight WestJet**

**Option 1: Bold Label**
- Click WestJet label
- Make font bold, larger (14pt), different color

**Option 2: Add Arrow**
- Insert → Shapes → Arrow
- Point to WestJet bubble
- Add text box: "Only airline in Growth + Profitability quadrant"

**Option 3: Glow Effect**
- Click WestJet bubble
- Format Data Point → Glow
- Add subtle glow effect

---

## **Final Chart Should Show:**

### **Quadrant Breakdown:**

```
        High ROA (+3% or more)
              │
   Singapore  │  WestJet
   (shrinking)│  (GROWING - only one!)
              │
──────────────┼────────────────
 Shrinking    │    Growing
   Assets     │     Assets
              │
  Air Canada  │  Continental
  (distressed)│  (growing into loss)
              │
        Low ROA (negative)
```

### **Key Visual Elements:**

✓ WestJet: Smallest bubble (C$2.08B) but in BEST position (top-right)
✓ Lufthansa: Largest bubble ($34.87B) but stuck at center (flat growth)
✓ Continental: Large bubble growing but losing money (danger zone)
✓ Singapore: Large bubble, profitable but shrinking (defensive)
✓ Southwest: Large bubble, shrinking fast (largest negative growth)
✓ Air Canada: Medium bubble in worst position (bottom-left)

---

## **Alternative: Manual Excel Setup**

If automatic bubble chart doesn't work well:

### **Create Scatter Plot First:**

1. Create scatter plot with X = Asset Growth, Y = ROA
2. Plot all 6 airlines as points
3. Then manually adjust each point to be a circle
4. Format each circle:
   - Size proportional to revenue
   - WestJet: Small circle (2.08)
   - Lufthansa: Largest circle (34.87)

### **Size Reference:**
- WestJet: 2.08B → 50pt circle
- Southwest: 11.02B → 150pt circle
- Lufthansa: 34.87B → 300pt circle
- Scale proportionally

---

## **Data Verification:**

### **Check Your Chart Against This:**

| Airline | X Position | Y Position | Bubble Size (Relative) | Color |
|---------|------------|------------|----------------------|-------|
| WestJet | +9.9 (far right) | +5.4 (top) | Smallest (2.08B) | Blue |
| Southwest | -14.7 (far left) | +1.2 (slightly above zero) | Large (11.02B) | Blue |
| Continental | +4.8 (right) | -4.6 (below zero) | Large (15.24B) | Red |
| Lufthansa | +0.4 (center) | +2.7 (middle) | Largest (34.87B) | Blue |
| Singapore | -6.4 (left) | +4.6 (high) | Large (10.53B) | Blue |
| Air Canada | -4.0 (left) | -9.0 (bottom) | Medium (8.35B) | Red |

---

## **Common Excel Issues & Fixes:**

### **Problem 1: Bubbles Too Small/Large**
- Right-click bubbles → Format Data Series
- Adjust "Scale bubble size to" percentage (try 50%, 75%, 100%, 150%)

### **Problem 2: Bubbles Overlap**
- Acceptable for this chart (shows reality)
- Or adjust chart size (make wider/taller)

### **Problem 3: Can't Add Airline Names**
- Manually add text boxes with airline names
- Position next to each bubble

### **Problem 4: Colors Not Working**
- Click individual bubbles one at a time
- Format Data Point → Fill → Solid Fill → Choose color

### **Problem 5: Axes Scale Wrong**
- Right-click axis → Format Axis
- Manually set min/max values
- X: -16 to +12
- Y: -10 to +6

---

## **PowerPoint Export Tips:**

If presenting this chart:

1. **Save as high-resolution image**
   - Right-click chart → Save as Picture
   - Format: PNG, 300 DPI

2. **Animation suggestions:**
   - Appear bubbles one by one
   - Start with quadrant labels
   - Then add bubbles from worst (bottom-left) to best (top-right)
   - WestJet appears last with emphasis

3. **Slide layout:**
   - Chart takes 70% of slide
   - Key insight box on right: "WestJet: Only airline achieving profitable growth"

---

## **Interpretation Guide for Audience:**

### **How to Read This Chart:**

**X-Axis (Left/Right):**
- Right = Growing assets (adding planes, capacity)
- Left = Shrinking assets (cutting capacity)

**Y-Axis (Up/Down):**
- Up = High profitability per dollar of assets
- Down = Losing money on assets

**Bubble Size:**
- Larger = Bigger airline by revenue
- Smaller = Smaller airline by revenue

**Color:**
- Blue = Profitable in 2008
- Red = Lost money in 2008

### **The Story:**

**WestJet (small blue bubble, top-right):**
Smallest airline but ONLY one in the "Growth + Profitability" quadrant. Growing assets (+9.9%) while maintaining highest return on assets (5.4%).

**Singapore (large blue bubble, top-left):**
Profitable (4.6% ROA) but shrinking assets (-6.4%). Defensive posture during crisis.

**Continental (large red bubble, bottom-right):**
Growing assets (+4.8%) but losing money on every dollar invested (ROA -4.6%). Growing into losses.

**Air Canada (medium red bubble, bottom-left):**
Worst position - shrinking AND unprofitable. Distressed.

**Key Insight:**
Size doesn't guarantee success. WestJet's small size and flexible business model positioned it to grow profitably when giants struggled.

---

## **Key Metrics Summary Table (Add Below Chart):**

| Airline | Size (Revenue) | Asset Growth | ROA | Position |
|---------|---------------|--------------|-----|----------|
| WestJet | $2.08B (Smallest) | +9.9% (Best) | 5.4% (Best) | Growth + Profit |
| Lufthansa | $34.87B (Largest) | +0.4% (Flat) | 2.7% (Moderate) | Stagnant |
| Singapore | $10.53B (Large) | -6.4% (Shrinking) | 4.6% (Good) | Defensive |
| Southwest | $11.02B (Large) | -14.7% (Worst) | 1.2% (Low) | Retreating |
| Continental | $15.24B (Large) | +4.8% (Growing) | -4.6% (Loss) | Dangerous |
| Air Canada | $8.35B (Large) | -4.0% (Shrinking) | -9.0% (Worst) | Distressed |

---

## **Success Criteria:**

Your final chart should clearly show:

✓ WestJet isolated in top-right quadrant (alone in best position)
✓ Four quadrants clearly labeled
✓ Bubble sizes proportional to revenue (Lufthansa largest, WestJet smallest)
✓ Colors distinguish profitable (blue) vs loss-making (red)
✓ Airline names clearly visible on/near each bubble
✓ Axes properly scaled with gridlines
✓ Zero lines (X=0, Y=0) visible as reference

**The visual punchline:** Small blue dot in top-right corner beats all the giants.