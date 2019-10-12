
#Scatter plots are just like regular line graphs which uses the X and Y axes to plot the 
#input data. It is used in situations where we want to show the correlation between one and another.

#Syntax: 

#matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None,
#vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs)

# Here, s represents the Marker Size and c represents the marker color.

import matplotlib.pyplot as plt
import numpy as np

n =100
X = np.random.normal(0,1,n)
X
Y = np.random.normal(0,1,n)
Y
colors=np.random.rand(n)

plt.scatter(X, Y, s=400, alpha=0.5,c=colors,edgecolors='yellow')

plt.xlim(-1.5, 1.9)
#plt.xticks(())
plt.ylim(-1.5, 1.5)
#plt.yticks(())

plt.show()