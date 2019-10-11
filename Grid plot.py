#Creating the gridlines in the plot gives us the visualisation of coordinate points clearly.

#Syntax: 

#matplotlib.pyplot.grid(b=None, which='major', axis='both', **kwargs)¶
#You can always turn the axes grids on or off by passing the argument b 
#which is a boolean value. 

#Now let us add the grid lines to the quiver plot

import matplotlib.pyplot as plt
import numpy as np

x,y = np.meshgrid(np.arange(0, 2*np.pi, .2), np.arange(0, 2*np.pi, .2))
x
y

u = np.cos(y)
v = np.sin(x)


plt.figure()
plt.quiver(x, y, u, v, scale=4, pivot='tip', units='x')
plt.scatter(x, y, color='r', s=10)
plt.grid(color='b', linestyle='-', linewidth=0.5)
plt.show()