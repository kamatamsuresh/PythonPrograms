import matplotlib.pyplot as plt

#Using the subplots, we can divide an area into multiple subplots in a grid. 
#We can do this by specifying the number of rows and columns and the number of plot.

#Here x and y must have same first dimension otherwise we get error.

x = range(10)
y = range(10)

fig,ax = plt.subplots(nrows=2, ncols=2) #Here fig should be mentioned.

for row in ax:
     for col in row:
        col.plot(x, y)

plt.show()

#Another way to show the same subplots

x = range(10)
y = range(10)

fig, ax = plt.subplots(nrows=2, ncols=2)

plt.subplot(2, 2, 1)
plt.plot(x, y)

plt.subplot(2, 2, 2)
plt.plot(x, y)

plt.subplot(2, 2, 3)
plt.plot(x, y)

plt.subplot(2, 2, 4)
plt.plot(x, y)

plt.show()

#-------------Axes function------------
#Many people confuse here with axes with axis. Axes is different than axis in matplotlib. 
#Axis represents the x-axis or the y-axis where as the axes means it is mostly like a subplots 
#which will allow the placement of those plots in any location within the figure or plot. 

#We can keep a small plot with in a bigger one or we can place two small plots side by 
#side with in the figure.

plt.axes([.8, .8, .5, .5])
plt.xticks(())
plt.yticks(())
plt.text(0.1, 0.1, 'axes([0.1, 0.1, .8, .8])', ha='left', va='center',
        size=16, alpha=.5)


plt.axes([.2, .2, .5, .5])
plt.xticks(())
plt.yticks(())
plt.text(0.1, 0.1, 'axes([0.2, 0.2, .5, .5])', ha='left', va='center',
        size=16, alpha=.5)

plt.plot(x, y)

plt.show()

