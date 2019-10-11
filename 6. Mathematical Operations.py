import numpy as np
#In Numpy, we can perform various Mathematical calculations using the various functions 
#that are provided in the library. Advanced Mathematical operations those can be performed 
#are Trigonometric functions, Hyperbolic functions, Rounding, Sums, Products, differences, 
#exponents, logarithms etc.

#Trigonometric Operations
np.sin(np.pi/2)
np.cos(np.pi/2)
np.tan(np.pi/2)

#Rounding Operations
x=np.array([-1.4, -1.1, -0.4, 0.7, 1.6, 1.9, 2.0])

print(np.floor(x))
print(np.ceil(x))
print(np.trunc(x))

#Sums and Differences
x=np.sum([[1,2],[3,4]])
x
y=np.sum([[1,2],[3,4]], axis=0) #axis=0 means based on columns
y
z=np.sum([[1,2],[3,4]], axis=1) #axis=1 means based on rows.
z

x=np.diff([[1,2],[3,4]])
x
y=np.diff([[1,2],[3,4]], axis=0)
y
z=np.diff([[1,2],[3,4]], axis=1)
z

#Logarithmic Operations
x=np.log([1]) #This will return the Natural logarithm, element-wise
x
y=np.log2([2,4,8]) #This will return the Base-2 logarithm of y.
y
