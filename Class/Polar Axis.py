#Polar function in matplotlib which can be integrated with pie chart or scatter 
#plot for best visual apperance of data in the angular nature using the polar axis coordinates.

import numpy as np
import matplotlib.pyplot as plt

#Below is the example to create a scatter plot on polar axis.

# Fixing random state for reproducibility
np.random.seed(1000000)

# Compute areas and colors
N = 150
r = 2 * np.random.rand(N)
r
theta = 2 * np.pi * np.random.rand(N)
theta
area = 200 * r**2
area
colors = theta

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
plt.show()

#Below is the example to create a pie chart on polar axis.

np.random.seed(19680801)

# Compute pie slices
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

plt.show()