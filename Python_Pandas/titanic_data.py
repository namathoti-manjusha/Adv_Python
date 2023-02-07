import pandas as pd
import numpy as nd
data=pd.read_csv("..//data/tested.csv")
#print(data.shape)
#print(data.isna().any())
#print(data.isna().sum())
#print(data.drop(["Cabin"],axis=1,inplace=True))
#print(data.fillna(method='ffill',inplace=True))
#print(data['Survived'].map({1:'yes',0:'no'}))
#print(pd.crosstab(index=data['Sex'],columns=data['Survived']))
#print(data.groupby(['Sex','Survived'])['Survived'].count())
#print(pd.pivot_table(data,index=['Sex','Age'],aggfunc=nd.sum))
print(data.sort_values(by=['Pclass','Age'],ascending=False))


