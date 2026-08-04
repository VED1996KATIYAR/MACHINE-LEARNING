
import pandas as pd

# 'Age' की गलती को 400 से बदलकर 40 कर दिया गया है
data1 = {"Name": ['Anna', 'Bob', "John"], "Age": [20, 40, 40], "score": [1, 2, 3]}
df1 = pd.DataFrame(data1)

print(df1)

data=[{'a':1,'b':2},{'a':7,'b':9}]
df2 = pd.DataFrame(data)
print(df2)
