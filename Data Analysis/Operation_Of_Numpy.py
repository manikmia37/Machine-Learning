import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

M1=np.array([[1,2,3],[4,5,6],[7,8,9]])
M2=np.array([[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]])
print(np.add(M1, M2))
print(np.subtract(M1, M2))
print(np.multiply(M1, M2))
print(np.divide(M1, M2))
print(np.sqrt(M1))

x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
print(x.dot(y))
print(np.dot(x,y))
print(x@y)
print(np.matmul(x,y))

v1=np.array([1,2,3]) # i+2j+3k
v2=np.array([-1,3,-2]) #-i+3j-2k
print(np.dot(v1,v2))

x=np.array([[1,2],[3,4],[5,6]])
print(x.shape)
v1=np.array([1,2,3]) 
print(v1.shape) # here 3 is number of column
print(np.dot(np.transpose(x),v1)) # As for multiplying, the number of columns have to be equal of the number of rows of second matrix

# Array created in new way
data1=np.arange(10) # The element of array will be from o to 9
print(data1)
print(np.average(data1))

data2=np.arange(12).reshape(4,3) # the value will be from 0 to 11 and the matrix size will 4 by 3
print(data2)

print(np.average(data2,axis=0)) # Column wise average
print(np.average(data2,axis=1)) # Row wise average

print(np.sum(data2))
print(np.sum(data2,axis=0))
print(np.sum(data2,axis=1))

# Create a matrix which all value will be 0 and the size will be 3 by 3
data3=np.zeros((3,3))
print(data3)

data4=np.random.rand(1,4)
print(data4)

data5=np.linspace(0,90,10).reshape(2,5)
print(data5)

data6=np.eye(4)  # Identity Matrix which size is 4 by 4
print(data6)