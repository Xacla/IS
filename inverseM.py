import numpy as np
import scipy.optimize as opti
import math
import matplotlib.pyplot as plt

def func(x, a, b):
    return a*x+b

def func_2(x, a, b,c):
    return a*x*x + b*c +c

A = np.loadtxt("lsmdata1_train.csv",delimiter=" ")
#A = np.loadtxt("lsmdata2_train.csv",delimiter=" ")

print(A)
x=A[:,0]
y=A[:,1]

A_coefficient,A_matrix=opti.curve_fit(func,x,y)
#A_coefficient,A_matrix=opti.curve_fit(func_2,x,y)
test_data=np.loadtxt("lsmdata1_test.csv",delimiter=" ")
#test_data=np.loadtxt("lsmdata2_test.csv",delimiter=" ")

print(A.shape)
print(A_coefficient)

a=A_coefficient[0]
b=A_coefficient[1]
#c=A_coefficient[2]

#culecurate RMS_of_training_data
data_sum=0
for i in range(A.shape[0]):
    y_true=A[i][1]
    y_Estimation=a * A[i][0] + b
    #y_Estimation=func_2(A[i,0],a,b,c)
    y_average=y_true - y_Estimation
    data_sum=pow(y_average,2)

data_sum=data_sum/A.shape[0]
#print(data_sum)
result = math.sqrt(data_sum)
print(result)

#culecurate RMS_of_test
data_sum=0
for i in range(A.shape[0]):
    y_true=test_data[i][1]
    y_Estimation=a * test_data[i][0] + b
    #y_Estimation=func_2(test_data[i,0],a,b,c)
    y_average=y_true - y_Estimation
    data_sum=pow(y_average,2)

data_sum=data_sum/A.shape[0]
#print(data_sum)
result = math.sqrt(data_sum)

print(result)
A=np.sort(A)
#print(A)

plt.axis([-10, 10, -10, 10])
#plt.plot(A[:,0],A[:,1] , "ro")
plt.plot(A[:,0],func(A[:,0],a,b),"g")
plt.plot(test_data[:,0],test_data[:,1] , "ro")
#plt.plot(test_data[:,0],func(test_data[:,0],a,b),"k")p
#plt.plot(A[:,0],func_2(A[:,0],a,b,c),"k")
plt.show()
