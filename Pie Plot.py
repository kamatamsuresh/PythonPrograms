#Pie plot is a kind of graphical representation in which a circle is divided into slices, 
#where each slice represents a numeric proportion of entire circle.

#Syntax

#matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, 
#       shadow=False, labeldistance=1.1, startangle=None, radius=None, counterclock=True, wedgeprops=None, 
#        textprops=None, center=(0, 0), frame=False, rotatelabels=False, hold=None, data=None)



import matplotlib.pyplot as plt

# In this Pie chart, slices will be plotted counter-clockwise.

labels = 'Mathematics', 'Physics', 'Chemistry', 'Biology'
sizes = [40, 20, 25, 15]
explode = (0.1, 0, 0, 0)  

plt.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%', shadow=True, startangle=90)

# Equal makes up a circle.

plt.axis('equal')
plt.show()

#Let us add a legend to the above pie chart with the help of plt.legend() function.

labels = 'Mathematics', 'Physics', 'Chemistry', 'Biology'
sizes = [40, 20, 25, 15]
explode = (0.1, 0, 0, 0)  

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

# Equal makes up a circle.

plt.axis('equal')
plt.legend(labels, loc="best")

plt.show()















