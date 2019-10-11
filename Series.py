import numpy as np
import pandas as pd
#Series is a one-dimensional labeled array capable of holding 
#any data type (integers, strings, floating point numbers, Python objects, etc.)
#Series created using ndarray

s = pd.Series(np.random.randn(4), index=['d', 'a', 't', 'a'])
s
s.index

#Series can be instantiated from dicts


d = {'d' : 0, 'a' : 1, 'c' : 2}
s1 = pd.Series(d)
s1
s1.index
pd.Series(d, index=['a', 'b', 'c', 'd'])


#Series created using scalar value
r=range(5)
type(r)
pd.Series(r, index=['a', 'b', 'c', 'd', 'e'])

r=range(5)
type(r)
pd.Series(r, index=['a', 'b', 'c', 'd'])




tp=('datascience','AI','ML','DL','NLP')
type(tp)
pd.Series(tp, index=['a', 'b', 'c', 'd', 'e'])


tp1=('datascience','AI','ML','DL')
type(tp1)
pd.Series(tp1, index=['a', 'b', 'c', 'd', 'e'])

lt=['datascience','AI','ML','DL','NLP']
type(lt)
pd.Series(lt, index=['a', 'b', 'c', 'd', 'e'])

lt=['datascience','AI','ML','DL']
type(lt)
pd.Series(lt, index=['a', 'b', 'c', 'd', 'e'])

#To access data using index
s
s.mean()
s[s < s.mean()]
s[:2]
s[:3]
np.exp(s)
s['d']
'f' in s
'a' in s
#Operations using Series
s * 2
s[1:] + s[:-1]


