#Quiver plot is used to display velocity vectors as arrows with components (u,v) 
#at the points (x,y).

#Syntax: 

#Axes.quiver(*args, data=None, **kw)

# Calling with different arguements

#quiver(U, V, **kw)
#quiver(U, V, C, **kw)
#quiver(X, Y, U, V, **kw)
#quiver(X, Y, U, V, C, **kw)

#U, V - Represents the Arrow data.
#X, Y - Represents location of arrows.
#C    - Represents the Color of arrows.

import matplotlib.pyplot as plt
import numpy as np

x,y = np.meshgrid(np.arange(0, 2*np.pi, .2), np.arange(0, 2*np.pi, .2))
u = np.cos(y)
v = np.sin(x)

plt.figure()
plt.quiver(x, y, u, v, scale=4, pivot='tip', units='x')
plt.scatter(x, y, color='r', s=5)
plt.show()