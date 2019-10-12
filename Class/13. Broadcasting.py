import numpy as np
#Numpy can transform the arrays of different sizes into the same sizes. 
#That kind of formulation or conversion is known as broadcasting in Numpy.

#Creating an array of size 1 column * 4 row
a=np.array([[0],[10],[20],[30],[40]])
a
a.shape

#Creating an array of size 3 column * 1 row
b=np.array([0,1,2])
b
b.shape

#Adding the both of them will give us the resultant Array after broadcasting
a+b
b+a
a-b
a*b