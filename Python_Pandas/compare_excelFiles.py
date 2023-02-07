import pandas as pd
import numpy as np
exldata1=pd.read_excel("C://data/myexcel.xlsx",sheet_name='Emp')
print(exldata1)
exceldata2=pd.read_excel('C://data/myexcel.xlsx',sheet_name='Deprtment')
print(exceldata2)
print(exldata1.compare(exceldata2))
data3=np.where(exldata1['Empid']==exceldata2['Empid'],True,False)
print(data3)