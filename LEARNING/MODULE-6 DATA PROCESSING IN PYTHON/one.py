import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/MY MEMORY/Complete tutetude/MACHINE LEARNING/LEARNING/MODULE-6 DATA PROCESSING IN PYTHON/Iris.csv");
print(df.head())
print(df.tail())
print(df.info())

print("Do it")

print(f"{df.shape[0]} rows and {df.shape[1]} columns")