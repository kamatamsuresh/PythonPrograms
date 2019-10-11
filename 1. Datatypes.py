import numpy as np

x=np.array([1,2,3,4,5])
x
type(x)
#we will use the "dtype" method to identify the datatype
x.dtype

x=np.array([1,2,3,4,5], dtype=float)#To assign the integers as float datatype
x
x.dtype
#This example will show the Boolean datatype
eq=np.array([True, False])
eq
type(eq)
eq.dtype
#This example will show the String datatype
str=np.array(["This","is","Numpy","in", "Data Science"])
str
str.dtype
#This example will show the Complex datatype

solve=np.array([2+3j, 5+2j, 9+3j])
solve
solve.dtype
solve.real

# guess the datatype by removing one by one element in the given array
y=np.array([1,1.1, "a",False])
y
y.dtype


# No Arrays in python unless you import the array module or import the numpy
import array as arr
a= arr.array('u',['1','3'])
a
