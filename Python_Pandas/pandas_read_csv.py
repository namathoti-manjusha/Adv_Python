import pandas as pd
data=pd.read_csv("..//data/train_and_test2.csv")
print(data)
#print(data.isna().any())
#print(data.isna().sum())
#tips_male_fm=data.filter(['tip','sex'])
#print(tips_male_fm.groupby('sex').sum())
#print(tips_male_fm.groupby('sex').count())
#print(data.describe())
#print(data.head(2))
#print(data.tail(3))