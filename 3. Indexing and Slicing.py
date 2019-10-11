import numpy as np
a=np.arange(5)
a
a[1]
a[2]
a[5] #Here we get error.(as 5th index does not exist)
a[-3]
a[-1]

#Now let us try with Multi-Dimensional Array
#We are creating an array with diag function to create a 3 by 3 matrix form
a=np.diag(np.arange(3))
a
a[0] #Means First row of all elements
## To access the column axis, we need to mention the specified index number to access the value
a[1,1]
a[1,3] #Here we get error.

#Accessing the column values from the matrix. we can use ellipsis(...) to get the column or row values in particular.
#If we place the ellipsis in the row position, it will get you the all the values of particular column
c=np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6]],int)
c
c[...,1]
c[1,...]
c[...,2]

#Accessing the row values from diagonal matrix.If we place the ellipsis in the column value 
#position, it will get you the all the values of particular row mentioned
c[1]
c[1,...]

#Slicing
a=np.arange(20)
a
a[5:20:5]
a[:4] #means from 0th index to before 4th index.
a[:10]
a[1:5] #means from first index to before 5th index.
a[5:] #means from 5th index to last index.
a[::4] #means multiples of 4 until last values.
a[0]















