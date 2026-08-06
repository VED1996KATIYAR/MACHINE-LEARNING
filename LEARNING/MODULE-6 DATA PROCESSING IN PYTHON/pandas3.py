import pandas as pd
data={'name':['Anna','Bob'],'age':[20,30],'score':[90,90]}
df=pd.DataFrame(data)
print(df)
print(df[0:1])

df.replace('Bob','Johnny',inplace=True)
print(df)

#mean
print(df['age'].mean())
#sum
print(df['age'].sum())
#min
print(df['age'].min())
#max
print(df['age'].max())

print(df.groupby('name')['age'].sum())

