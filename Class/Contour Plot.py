#Contour is nothing but the outlines or shape of something.
#Contour plots are isolines to represent the graphical 3-D surface by 
#plotting the Z slices. Simply we can say that Contour plots can be used to 
#show 3-Dimensional surfaces on a 2-Dimensional plane.

#------Syntax-----------
#To create a contour plot of an array Z. The level values are taken automatically by itself.
#contour(Z)

#To create a contour plot using the coordinates X, Y specify the (x, y) coordinates of the surface.
#contour(X,Y,Z)

#To contour up to N automatically-chosen levels.
#contour(Z,N)
#contour(X,Y,Z,N)

#To draw contour lines at specified values in sequence V in increasing order.
#contour(Z,V)
#contour(X,Y,Z,V)

#To fill the len(V)-1 regions between the values in V in increasing order.
#contourf(..., V)

import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (1 + x*2+ x *1 + y * 3) * np.exp(-x ** 2 -y ** 2)

n = 0.01

x = np.arange(-3.0, 3.0, n)
y = np.arange(-2.0, 2.0, n)
X, Y = np.meshgrid(x, y)
X
Y


plt.contourf(X, Y, f(X, Y), 8, alpha=.5, cmap='jet')
C = plt.contour(X, Y, f(X, Y), 8, colors='black')

plt.clabel(C, inline=1, fontsize=10)
plt.title('Simple Contour Plot with labels')

plt.show()

#When we want to plot the numpy arrays which consists some data as 
#images can be rendered using the function called imshow().

plt.imshow(f(X, Y))
