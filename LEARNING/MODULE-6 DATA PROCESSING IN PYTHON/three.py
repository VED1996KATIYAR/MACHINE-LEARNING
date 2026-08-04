#indexing and slicing in numpy
import numpy as np
# a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a1)
# print(a1[1,2])
# print(a1[0,1])
# print(a1[0:])
# print(a1[1:])
# print(a1[2:])

# a11=np.array([1,2,3])
# a12=np.array([4,5,6])
# print(a11+a12)
# print(a11-a12)
# print(a11*a12)
# print(a11/a12)
# print(a11**2)
#
#
# print(np.sqrt([1,4,9]))
# print(np.exp([1,4,9]))
#
# a=np.array([[1],[2],[3]])
# b=np.array([[4,5,6]])
# print(a+b)

aa=np.array([[1,2],[4,5],[7,8]])
print(aa.reshape(2,3)) #reshape the array into 2 rows and 3 columns
print(aa.flatten()) #reshape the elements in single row
