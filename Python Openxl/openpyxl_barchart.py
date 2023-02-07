from openpyxl.chart import BarChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sales_data=[['Product','online','Store'],[1,30,40],[2,50,60],[3,20,70],[4,20,43],[5,15,80],[6,65,72]]
for row in sales_data:
    sheet.append(row)
chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=7,min_col=2,max_col=3)
chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart,'E2')
wb.save("C://data//barchart.xlsx")