import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(a))#sum of aall elements in array
b=np.array([1,2,3,4,5])
print(np.mean(b))#mean of the array
print(np.min(b)) #min in array
print(np.max(b)) #max in array

a1=np.array([[1,2],[3,4]])
a2=np.array([[5,6],[7,8]])
print(a1.dot(a2))