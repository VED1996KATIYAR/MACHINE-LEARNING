#pandas
import pandas as pd

s=pd.Series([1,2,3,4,5])
print(s)

a=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(a)


#create a dataframe means 2d data in key-value form
data={"Name":['Anna','Bob'],"Age":[20,40]}
df=pd.DataFrame(data)
print(df)


