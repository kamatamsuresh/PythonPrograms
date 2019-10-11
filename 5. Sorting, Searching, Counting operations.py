import numpy as np
#In Numpy, we can perform various Sorting, Searching, Counting operations using the various 
#functions that are provided in the library like sort, argmax, argmin, count_nonzero etc.

#sort: This will return a sorted copy of an array.
#argmax: This will return the indices of the maximum values along an axis.
#argmin: This will return the indices of the minimum values along an axis. 
#count_nonzero: This will return count of number of non-zero values in the array.

x=np.array([[2,7,15],[9,1,12],[16,6,1]])
x

# row wise sorting 
np.sort(x)

#flattened and sorted
np.sort(x,axis=None)

np.sort(x.ravel())

# Columns wise
np.sort(x,axis=0)
x

# Row wise
np.sort(x,axis=1)


x=np.array([[6,4],[3,2]])
x
#np.sort(x,axis=0)
np.sort(x)
np.sort(x,axis=None)
x
np.sort(x,axis=0)
np.sort(x,axis=1)

x
np.argmax(x, axis=0)
np.argmax(x, axis=1)
np.argmin(x, axis=0)
np.argmin(x, axis=1)

y=np.array([[213,873],[323,291]])
y
np.argmax(y)

np.argmax(y, axis=0)
np.argmax(y, axis=1)
np.argmin(y, axis=0)
np.argmin(y, axis=1)

z=np.array([[1,2,3],[3,4,5]])
z
np.argmax(z)
np.argmax(z, axis=0)
np.argmax(z, axis=1)
np.argmin(z, axis=0)
np.argmin(z, axis=1)


y=np.array([[6,4],[3,2],[1,2]])
y
np.argmax(y)
np.argmax(y, axis=0)
np.argmax(y, axis=1)
np.argmin(y, axis=0)
np.argmin(y, axis=1)

np.eye(4)
np.count_nonzero(np.eye(4))
np.eye(10)
np.count_nonzero([[0,1,7,0,0],[3,0,0,2,19]])

#---------------NumPy - Matrix Library-----------------

#Matrix - This will return a matrix from an array kind of an object or from the string of data.

x=np.matrix('1,2,3,4')
x
#asmatrix - This will interpret the input as matrix.
x=np.array([[1,2],[3,4],[4,5]])
x
y=np.asmatrix(x)
y

