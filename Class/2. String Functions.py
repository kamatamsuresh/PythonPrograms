import numpy as np
#In Numpy, we can handle the string operations with provided functions

#1. add: This will return element-wise string concatenation for two arrays of str
x=np.array(("iam a numpy"))
y=np.array(("program"))
np.char.add(x,y)

#multiply: This will return element-wise string multiple concatenation
x=np.char.multiply("numpy",5)
x

#capitalize: This will return a copy of string with first character of each element capitalized.
x=np.char.capitalize("numpy")
x

#split: This will return a list of words in the string
x=np.char.split("iam a numpy program")
print(x)

#lower: This will return an array with elements converted to lowercase
x=np.char.lower("NUMPY")
x

#upper: This will return an array with elements converted to uppercase
x=np.char.upper("numpy")
x

#equal: This will return a element-wise comparision
x=np.char.equal("iam","numpy")
x

#not_equal: This will return a element-wise comparision
x=np.char.not_equal("iam","numpy")
x

#count: This will return an array with the number of non-overlapping occurances 
#of substring in the range
x=np.array(['bet','abet','alphabet'])
x
np.char.count(x,'bet')
np.char.count(x,'abet')
np.char.count(x,'alphabet')

#isnumeric: This will return true if there is only numeric characters in the element
np.char.isnumeric('bet')

#rfind: This will return the highest index in the string where substring is found
x=np.array(['bet','abet','alphabet'])
np.char.rfind(x,'abet')
np.char.rfind(x,'bet')
np.char.rfind(x,'alphabet')









