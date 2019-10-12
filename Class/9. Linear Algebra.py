import numpy as np

#----------Performing Linear Algebra on several matrices which are stacked as an array------

#dot: This will return the dot product of two arrays.
np.dot(5,4)
a=[[1,2],[3,4]]
b=[[4,2],[1,3]]
np.dot(a,b)

#vdot: This will return the dot product of two vectors.
a
type(a)
b
np.vdot(a,b) #This is how it works in the above example ==> 

#inner: This will return the inner product of two arrays.
a=[[1,2,3],[0,1,1]]
b=[[1,2,3],[0,0,1]]
a
b
np.inner(a,b)

#outer: This will return the outer product of two vectors.
a=[[1,2],[3,4]]
b=[[4,3],[2,1]]
a
b
np.outer(a,b)
np.outer(b,a)

#matmul: This will return the matrix product two arrays.
a=[[1,2],[3,4]]
b=[[1,1],[1,1]]
np.matmul(a,b)

 #2x2 1x2 = 1x2    1x2 2x2 = 1x2
a=[[1,2],[3,4]]
b=[1,1]
a
b
np.matmul(a,b)
np.matmul(b,a)

#tensordot: This will return the computed tensor dot product along specific aces for arrays>=1-D.
#a = [1, 1, 0],[1, 0, 1]
#b = [[1],[0]],
#    [[0],[0]],
#    [[1],[0]]

x=np.random.randint(2000,9000)
x

a=np.random.randint(3, size=(2,3,4))
a
a.shape
a.ndim

b=np.random.randint(2, size=(4,3,2))
b
b.shape

c=np.tensordot(a,b,axes=1)
c
c.shape
c.ndim

np.tensordot(a,b,axes=((1),(1))).shape
#Here we have choosen 1, 1 axes 
# In a ==> (1,2,3), b===> (3,2,1)===> ignore 2 now ===> (1,3,3,1)

x=np.array(range(1,9))
x
x.shape=(2,2,2)
x
#
X=np.array(('a','b','c','d'),dtype=object)
X
X.shape=(2,2)
X
#x
#
np.tensordot(x,X)
#np.tensordot(x,X,1)
#np.tensordot(x,X,0)
#np.tensordot(x,X,((0,1),(0,1)))
#np.tensordot(x,X,(2,1))
#




