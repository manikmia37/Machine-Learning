import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

# Create Two Dimentional Array

list1=[[1,0],[1,1],[2,2],[2,3],[2,3],
       [2,4],[3,4],[3,5],[4,6],[5,7]]
print(list1)

# Create DataFrame from list1
# df_list1=pd.DataFrame(list1)
df_list1=pd.DataFrame(list1, columns=['X','Y'])
print(df_list1)

# Draw histogram
df_list1.hist(column='X', bins=5)
#plot.show()
df_list1.hist(column='Y', bins=8)
#plot.show()

# Series 
print(df_list1[['X']])

# Skew
print('Skew: ',df_list1[['X']].skew())
print('Skew: ',df_list1[['Y']].skew())

# kurt
print('Kurt-x',df_list1[['X']].kurt())
print('Kurt-x',df_list1[['Y']].kurt())

df_list1.plot.scatter(x='X',y='Y')
#plot.show()
df_list1.boxplot(column=['X','Y'])
#plot.show()


# All about numpy

# Create Numpy Array
A=np.array([1,2,3,4,5,6])
print(A)
# print(type(A))

B=np.array([10,20,30,40,50,60])
print(B)

print(A+B)
print(A-B)
# Create List
list1=[1,2,3,4,5,6]
print(list1)
list2=[10,20,30,40,50,60]
print(list2)
print(list1+list2) 
""" print(list1-list2) as python doesnot suport '-' symbol 
so we have to follow another way for subtract and in addition. it is not a additon of value"""
print([x-y for x,y in zip(list1,list2)])

# Create Matrix
M1=np.array([[1,2,3],[4,5,6]])
print(M1)
print(M1.shape)
M2=np.array([[7,8,9],[10,11,12]])
print(M2)

# Matrix operation
print(M1+M2)
print(M1-M2)
print(M1*M2)
print(M1/M2)

M1=np.array([[1,2,3],[4,5,6],[7,8,9]])
#slice the three rows with first two rows
M7=M1[:,0:2]
print(M7)

#slice the last row with last two columns
M8=M1[-1,-2:]
print(M8)

M9=np.array([[1,2,3,4],[56,43,23,78],[100,101,102,103]])
bool_idx=(M9%2==0)