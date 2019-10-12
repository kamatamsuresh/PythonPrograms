import numpy as np
#To Create an One-Dimensional(1-D) Array
a=np.array([1,2,3,4],float)
a
type(a)
a.ndim # ndim will be used to find the type of dimension of that array
a.shape #shape property will be used to find out the size of each array dimension
len(a) #len function will be used to get the length of first array axis in the dimension


a1=np.array([[1,2,3,4],],float)
a1.shape
a1.ndim

#let us see creating an Two-Dimensional(2-D) Array
b=np.array([[1,2,3,4],[5,6,7,8]],int)
b
type(b)
b.ndim
b.shape
len(b)

# Creating an Two-Dimensional(2-D) Array 
c=np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6]],int)
type(c)
c
c.ndim
c.shape
len(c)
#Accessing the values in above Two-Dimensional Array

c[1,1]
c[2,3]
c[2,0]
c[0,0]
c[0,3]

#We can reshape an array using the reshape function
d=c.reshape(4,3)
d
d=c.reshape(2,6)
d
d=c.reshape(1,12)
d

# Error of Shape validation
--d=c.reshape(3,3) 
--d

#Numpy - Array using arange function
a=np.arange(5)
a
a[2]
a[4]

b=np.arange(0,20,5)#Here first argument is start number ,second is ending number, third is nth position number
b
b[2]
#If you want to divide it by number of points, linspace function can be used
b=np.linspace(0,1,100)
b

b1=np.linspace(0,1,7)
b1

#Creating Arrays using other functions like ones, zeros, eye
a=np.ones([3,3])
a
a1=np.zeros([2,3])
a1
np.ones(5)
np.eye(3)

np.eye(16)
















