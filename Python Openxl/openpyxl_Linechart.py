from openpyxl.chart import LineChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sales_data=[['Years','Sales'],[2010,2000],[2011,4000],[2012,6000],[2013,3000],[2014,5000],[2015,8000],[2016,7000],[2017,3000],[2018,2000]]
for row in sales_data:
    sheet.append(row)
chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=9,min_col=1,max_col=2)
chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart,'E2')
wb.save("C://data//linechart.xlsx")