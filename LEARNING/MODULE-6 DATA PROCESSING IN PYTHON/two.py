import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(arr.ndim) #no of the rows
print(arr.shape) #no dimensions(i*j)
print(arr.size) # size of array
print(arr.dtype)#data type


b=np.array([[1,2],[3,4],[5,6]])
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)

c=np.arange(0,10,2)
print(c)

#create arrays
d=np.zeros((3,4)) # it creates array with 3 rows and 4 columns
print(d)


d=np.ones((3,4)) #it creates arrays with 3 rows and 4 columns
print(d)

e=np.eye(3)
print(e)

