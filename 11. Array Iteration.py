
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10],int)
a
# iterate over the array a of integer numbers
for i in a:
	print (i)
#In Multi-dimensional Array
    #The iteration will go over the first axis 
    #so that each loop returns you the subset of the array
a=np.array([[1,2],[3,4],[5,6],[7,8],[9,10]],int)
a
a.ndim
# Iterating Through 2-D Array
for i in a:
	print (i)

# Doing the calculation along with the array iteration
for (i,j) in a:
	print (i+j)
    
#Let us work with the 2-Dimensional Array.
a=np.array([[1,2,3],[4,5,6],[7,8,9]],int)
a
# Iterating Through 2-Dimensional Array
for i in a:
	print (i)
    
for (x,y,z) in a:
	print (x+y+z)
    
for (x,y,z) in a:
    print (x*y*z)   
    

x=np.ones((3,3,3,3))   
x
x.ndim

a= np.array([[  [23, 234, 91], [123, 23, 45 ]   ] , 
   [  [23, 234, 91], [123, 23, 45 ]   ]])
a
a.shape
a.ndim
    
    
    
    
    
    
    
    
    
    
    
    
    