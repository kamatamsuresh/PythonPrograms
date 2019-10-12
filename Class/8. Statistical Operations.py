import numpy as np
#In Numpy, we can perform various statistical calculations using the various functions that are
#provided in the library like Order statistics, Averages and variances, correlating, Histograms

#------Order statistics------
#amin: This will return the minimum of an array.
#amax: This will return the maximum of an array.

x=np.arange(5,9).reshape((2,2))
x
np.amin(x)
np.amin(x, axis=0)
np.amin(x, axis=1)
np.amin(x, axis=2)
np.amax(x)
np.amax(x, axis=0)
np.amax(x, axis=1)

#------Averages and variances----

#median: This will return the median along the specified axis.
#average: This will return the weighted average along the specified axis.
#mean: This will return the arithmetic mean along the specified axis.
#std: This will return the standard deviation along the specified axis.
#var: This will return the variance along the specified axis.

x=np.array([[1,2,3],[4,5,6]])
x
np.median(x)
np.median(x,axis=0)
np.average(x)
np.mean(x)
np.std(x)
np.var(x)





