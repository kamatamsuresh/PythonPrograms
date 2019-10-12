import numpy as np
#We can change the array shape using the Array manipulation routines like reshape and ravel. 
#reshape: This will give us the new shape for an array without changing its data
#ravel: This will return the contiguous flattened array.
#We can transpose an array using the ndarray.T Operation which will be same if self.ndim is less than 2

# creating array of 2 * 3 dimension
a=np.array([[1,2,3],[4,5,6]])
a
# using ravel to flatten the array
b=a.ravel()
b
len(b)
# transpose the array from 2 * 3 dimension to 3 * 2 dimension
a.T
# ravel the transposed array
a.T.ravel()
# Using the reshape option to revert from ravel
a.T.ravel().reshape((2,3))

#Using the shape and reshape
a=np.arange(4*3*2)
a
a1=a.reshape(4,3,2)
a1
a1.shape
a2=a1.T
a2
a2.shape
a2


b=np.array([1,2,3,4])
b
b.shape
b1=np.array([[1,2,3,4]])
b1
b1.shape
b.T
b.reshape(2,2)
c=b.reshape(2,2)
c.T

