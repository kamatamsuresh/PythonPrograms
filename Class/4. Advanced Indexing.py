import numpy as np
x=np.array([[1,2],[3,4],[5,6]])
x
#Let us try to select specific elements like [0,1,2] 
#which is a row index and column index [0,1,0] each element for the corresponding row
x[[0,1],[1,1]]
x[[0,1,2],[0,1,0]]

x[0] #It gives you the first row
x[[0],[1]] #Here 0 acts as row index and 1 acts as column index 
x[[0],[2]] #Here we get an error.
x[[0],[1]]+1 #We can do add operations
x[[0],[1]]+=1 #This operation will change the values in the array and returns the new copy of an array
x
x[0]+=1 #Adding 1 to entire row.
x

#Boolean Indexing
x=np.array([[0,1,2],[3,4,5],
	    [6,7,8],[9,10,11]])
x
x[x ==15] #returns the values which are 0.
x[x%2!=0] # returns the values which are even numbers.
