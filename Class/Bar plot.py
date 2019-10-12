#Bar plots are used to represent comparision between the data points using the bars 
#either horizontally or vertically

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
money = [1, 2, 5, 6]

plt.ylabel('Millions')
plt.xlabel('Top Tycoons')
plt.title('Richest in the World')

plt.bar(x, money)
plt.xticks(x, ('Gates', 'Warren', 'Mittal', 'Ambani'))
plt.show()

#-------------
#import sys
#y=range(100000)
#sys.getsizeof(y)
#z=np.arange(100000)
#sys.getsizeof(z)

