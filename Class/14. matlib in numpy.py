import numpy.matlib as mb
#----some replacement functions in matlib----

#empty: This will return a new matrix of given shape and type
# Below function will generate the random data
mb.empty((2,2))
mb.empty((2,2),int)
mb.empty((2,2),int)



#zeros: This will return a matrix of given shape and type, filled with zeros.
mb.zeros((3,3))
mb.zeros((3,3),int)

#ones: This will return a matrix of ones.
mb.ones((3,3))
mb.ones((3,3),int)

#eye: This will return a  matrix with ones on diagonal and zeros elsewhere.
mb.eye(3)
mb.eye(3,dtype=int)

#identity: This will return a square identity matrix of given size.
mb.identity(3,dtype=int)
mb.identity(4,dtype=int)

#rand: This will return a matrix of random values with given shape.
mb.rand(2,3) # if the first argument is tuple, Other arguments are ignored.
