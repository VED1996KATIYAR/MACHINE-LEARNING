import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
#line
plt.plot(x,y,color='red',linestyle='dotted',marker='o',linewidth=2)
plt.title('Basic line plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#bar chart
categories=['A','B','C','D','E','F']
values=[10,20,30,40,50,60]
plt.bar(categories,values)
plt.title('bar chart')
plt.xlabel('categories')
plt.ylabel('values')
plt.show()

#SCATTER PLOT
x=[1,4,5,7,8,9]
y=[4,7,9,2,1,8]
plt.plot(x,y,color='black')
plt.title('line plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()