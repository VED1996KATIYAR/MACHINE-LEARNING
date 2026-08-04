import pandas as pd

data={'name':['Anna','Bob'],'age':[20,30],'score':[90,90]}
df=pd.DataFrame(data)
print(df)
print(df['name'])
print(df[['age','score']])

print(df[0:2])
print(df.iloc[0:2])
print((df['age']>20) & (df['score']>1))

print(df.isnull())#to check whteher the data has null values pr not
print(df.dropna()) # to remove null values
print(df.fillna(0))# if there is null values replace it with 0


print(df.rename(columns={'name':'Fullname'},inplace=True))#to replace the columns names
print(df)