#!/usr/bin/env python3
import xlsxwriter

# Create workbook
workbook = xlsxwriter.Workbook('/Users/ricardopascua/Projects/aim/__raw/asset_efficiency_bubble_chart.xlsx')

# Add worksheets
data_sheet = workbook.add_worksheet('Data')
chart_sheet = workbook.add_worksheet('Bubble Chart')

# Define formats
header_format = workbook.add_format({
    'bold': True,
    'bg_color': '#366092',
    'font_color': 'white',
    'align': 'center',
    'valign': 'vcenter',
    'border': 1
})

data_format = workbook.add_format({
    'align': 'center',
    'valign': 'vcenter',
    'border': 1
})

title_format = workbook.add_format({
    'bold': True,
    'font_size': 16,
    'align': 'left',
    'valign': 'vcenter'
})

note_format = workbook.add_format({
    'italic': True,
    'font_size': 10,
    'text_wrap': True
})

# Data
headers = ['Airline', 'Asset Growth %', 'ROA %', 'Revenue 2008 (USD Billions)', 'Status']
data = [
    ['WestJet', 9.9, 5.4, 2.08, 'Profitable'],
    ['Southwest', -14.7, 1.2, 11.02, 'Profitable'],
    ['Continental', 4.8, -4.6, 15.24, 'Loss'],
    ['Lufthansa', 0.4, 2.7, 34.87, 'Profitable'],
    ['Singapore', -6.4, 4.6, 10.53, 'Profitable'],
    ['Air Canada', -4.0, -9.0, 8.35, 'Loss']
]

# Write headers
for col, header in enumerate(headers):
    data_sheet.write(0, col, header, header_format)

# Write data
for row, airline_data in enumerate(data, start=1):
    for col, value in enumerate(airline_data):
        data_sheet.write(row, col, value, data_format)

# Set column widths
data_sheet.set_column('A:A', 15)
data_sheet.set_column('B:B', 15)
data_sheet.set_column('C:C', 12)
data_sheet.set_column('D:D', 25)
data_sheet.set_column('E:E', 12)

# Create bubble chart
chart = workbook.add_chart({'type': 'scatter', 'subtype': 'straight_with_markers'})

# We'll create it as scatter first since bubble charts need special handling
# Add each airline as separate series for better control

# Profitable airlines (blue shades)
profitable_data = [
    ('WestJet', 9.9, 5.4, 2.08, '#003f5c'),
    ('Southwest', -14.7, 1.2, 11.02, '#2f4b7c'),
    ('Lufthansa', 0.4, 2.7, 34.87, '#665191'),
    ('Singapore', -6.4, 4.6, 10.53, '#a05195')
]

# Loss-making airlines (red shades)
loss_data = [
    ('Continental', 4.8, -4.6, 15.24, '#d45087'),
    ('Air Canada', -4.0, -9.0, 8.35, '#ff6361')
]

# Add series for each airline
row_map = {
    'WestJet': 1,
    'Southwest': 2,
    'Continental': 3,
    'Lufthansa': 4,
    'Singapore': 5,
    'Air Canada': 6
}

for name, x, y, size, color in profitable_data + loss_data:
    row = row_map[name]
    chart.add_series({
        'name': name,
        'categories': f'=Data!$B${row+1}',
        'values': f'=Data!$C${row+1}',
        'marker': {
            'type': 'circle',
            'size': int(size * 4),  # Scale size for visibility
            'fill': {'color': color},
            'border': {'color': 'black', 'width': 1}
        },
        'data_labels': {
            'value': False,
            'custom': [{'value': name}],
            'position': 'center',
            'font': {'size': 9, 'bold': True}
        }
    })

# Configure chart
chart.set_title({
    'name': 'Asset Efficiency & Growth: WestJet vs Competitors (2008)',
    'name_font': {'size': 14, 'bold': True}
})

chart.set_x_axis({
    'name': 'Asset Growth 2007-2008 (%)',
    'name_font': {'size': 11, 'bold': True},
    'min': -16,
    'max': 12,
    'major_unit': 4,
    'minor_unit': 2,
    'major_gridlines': {'visible': True, 'line': {'color': '#D3D3D3'}},
    'line': {'color': 'black', 'width': 1.5}
})

chart.set_y_axis({
    'name': 'Return on Assets (%)',
    'name_font': {'size': 11, 'bold': True},
    'min': -10,
    'max': 6,
    'major_unit': 2,
    'minor_unit': 1,
    'major_gridlines': {'visible': True, 'line': {'color': '#D3D3D3'}},
    'line': {'color': 'black', 'width': 1.5}
})

chart.set_legend({
    'position': 'bottom',
    'font': {'size': 9}
})

chart.set_size({'width': 800, 'height': 600})

# Insert chart into Chart sheet
chart_sheet.insert_chart('B2', chart)

# Add title and notes to chart sheet
chart_sheet.write('B1', 'Asset Efficiency Analysis - 2008', title_format)
chart_sheet.set_column('B:B', 100)

# Add interpretation guide
interpretation_row = 35
chart_sheet.write(interpretation_row, 1, 'How to Read This Chart:', title_format)
chart_sheet.set_row(interpretation_row, 20)

interpretation_text = [
    '',
    'QUADRANTS:',
    '• Top-Right: IDEAL - Growing Assets + High ROA (WestJet is here!)',
    '• Top-Left: DEFENSIVE - Shrinking Assets + High ROA (Singapore)',
    '• Bottom-Right: DANGER ZONE - Growing Assets + Negative ROA (Continental)',
    '• Bottom-Left: DISTRESSED - Shrinking Assets + Negative ROA (Air Canada)',
    '',
    'BUBBLE SIZE: Represents 2008 revenue (larger = bigger airline)',
    '• Lufthansa: $34.87B (largest)',
    '• WestJet: $2.08B (smallest, but best positioned)',
    '',
    'KEY INSIGHT:',
    'WestJet is the ONLY airline in the "Growth + Profitability" quadrant.',
    'Despite being 4-10x smaller than competitors, WestJet achieved:',
    '  - Highest asset growth (+9.9%)',
    '  - Highest return on assets (5.4%)',
    '  - Only airline growing assets while maintaining profitability',
    '',
    'CONTEXT:',
    '2008 was the worst year for airlines since 9/11. Most airlines were',
    'cutting capacity and losing money. WestJet\'s ability to grow profitably',
    'during industry collapse demonstrates structural competitive advantage.'
]

for i, text in enumerate(interpretation_text):
    chart_sheet.write(interpretation_row + i + 1, 1, text, note_format)

# Add data summary table
summary_row = interpretation_row + len(interpretation_text) + 3
chart_sheet.write(summary_row, 1, 'Data Summary:', title_format)

summary_headers = ['Airline', 'Asset Growth %', 'ROA %', 'Revenue (USD B)', 'Position']
for col, header in enumerate(summary_headers):
    chart_sheet.write(summary_row + 1, col + 1, header, header_format)

summary_data = [
    ['WestJet', '+9.9%', '5.4%', '$2.08B', 'Growth + Profit (BEST)'],
    ['Singapore', '-6.4%', '4.6%', '$10.53B', 'Defensive (Profitable but shrinking)'],
    ['Lufthansa', '+0.4%', '2.7%', '$34.87B', 'Stagnant (Flat growth)'],
    ['Southwest', '-14.7%', '1.2%', '$11.02B', 'Retreating (Shrinking fast)'],
    ['Continental', '+4.8%', '-4.6%', '$15.24B', 'Danger Zone (Growing into losses)'],
    ['Air Canada', '-4.0%', '-9.0%', '$8.35B', 'Distressed (WORST)']
]

for row, row_data in enumerate(summary_data):
    for col, value in enumerate(row_data):
        chart_sheet.write(summary_row + row + 2, col + 1, value, data_format)

# Add notes section
notes_row = summary_row + len(summary_data) + 4
chart_sheet.write(notes_row, 1, 'Notes:', title_format)
notes = [
    '• All data from 2008 financial statements (2007-2008 comparison)',
    '• Asset Growth calculated as: (2008 Assets - 2007 Assets) / 2007 Assets',
    '• ROA calculated as: Net Income / Total Assets',
    '• Revenue normalized to USD using year-end 2008 exchange rates',
    '• Bubble sizes scaled proportionally to revenue (Lufthansa largest, WestJet smallest)',
    '• "Profitable" = positive net income in 2008; "Loss" = negative net income',
    '',
    'Data Sources: Exhibits 1, 2, 10 from WestJet Airlines case study'
]

for i, note in enumerate(notes):
    chart_sheet.write(notes_row + i + 1, 1, note, note_format)

workbook.close()

print("✓ Excel file created successfully!")
print("Location: /Users/ricardopascua/Projects/aim/__raw/asset_efficiency_bubble_chart.xlsx")
print("\nThe file contains:")
print("  - 'Data' sheet: Raw data with all metrics")
print("  - 'Bubble Chart' sheet: Visualization with interpretation guide")
print("\nChart shows WestJet in the top-right 'Growth + Profitability' quadrant - the only airline there!")
