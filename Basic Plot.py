import matplotlib.pyplot as plt
import numpy as np

#-------------Basic plotting---------
x=np.linspace(-np.pi, np.pi, 256, endpoint=True)
x
s, c=np.sin(x), np.cos(x)
plt.plot(x,c)
plt.plot(x,s)
plt.show()

#--------Color changes--------

#Let us make few changes like figure size, color of lines, line width etc 
#using the function "figure", "plot"

#In the figure function we can provide the size of the image output details and dpi value 
#which is dots per inch to increase visual quality.

#In the plot function , we can provide the line color and width for cos and sin curves. 

plt.figure(figsize=(7, 4), dpi=80)
plt.plot(x, c, color="green", linewidth=10, linestyle="-")
plt.plot(x, s, color="grey",  linewidth=5, linestyle="-")
plt.show()


#plt.figure(figsize=(20, 20), dpi=2000) #Dont give more size or dpi. Otherwise
# python gets stopped and we get as "Kernel died, restarting"

#------Ticks------------

#In Matplotlib, ticks are generally displayed as small marks on both X and Y axis as 
#reference points for plotting the curves.

#You can observe in our previous topic, the plot has 7 ticks on x axis and 9 ticks on Y axis.
#We can change those ticks using the xticks() and yticks() functions. 

plt.figure(figsize=(7, 4), dpi=70)
plt.plot(x, c, color="green", linewidth=20, linestyle="-")
plt.plot(x, s, color="black",  linewidth=5, linestyle="-")

plt.xticks([-np.pi, 0, np.pi])
plt.yticks([-1, 0, +1])
plt.show()

#----------------tick labels------------
#If you observe in the previous plot for ticks on X axis we have given -pi , 0 , pi 
#which are represented in numerical format. But i want to print the labels as 
#mathematical pi symbol.

#we have to use the latex to render the label as we required and we need provide 
#those values in the second argument list of correspoding label. 

plt.figure(figsize=(7, 4))
plt.plot(x, c, color="green", linewidth=20, linestyle="-")
plt.plot(x, s, color="black",  linewidth=5, linestyle="-")

plt.xticks([-np.pi, 0, np.pi],[r'$-\pi$',  r'$0$',  r'$+\pi$'])
plt.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])
plt.show()

#-----------Moving Spines------
#Spines are the lines which required to place at arbitrary positions that are connecting 
#the axis tick marks and noting the boundaries. 

#So, we have to move the lines or the axis behind our sin, cos curves where the left ones 
#will be the negative values and right ones will be the positive values for X axis. 
#For Y axis, negatives will be the down and positives will be on the upper side of the axis.

plt.figure(figsize=(10, 6), dpi=70)
plt.plot(x, c, color="green", linewidth=15, linestyle="-")
plt.plot(x, s, color="grey",  linewidth=10, linestyle="-")

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
#set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
#.set_position(('data',0))

plt.xticks([-np.pi, 0, np.pi],[r'$-\pi$',  r'$0$',  r'$+\pi$'])
plt.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])
plt.show()

#------------Adding a legend-------------
#In Matplotlib, legend is a function which is used to place the legend on the axes. 
#we can place the legend in various positions and can be placed either inside or 
#outside of the chart or plot.

#In our example, let us add the legend in the upper right corner. 

plt.figure(figsize=(10, 6), dpi=70)
plt.plot(x, c, color="green", linewidth=10, linestyle="-", label="cosine")
plt.plot(x, s, color="grey",  linewidth=10, linestyle="-", label="sine")

plt.legend(loc='upper left')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.xticks([-np.pi, 0, np.pi],[r'$-\pi$',  r'$0$',  r'$+\pi$'])
plt.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])
plt.show()