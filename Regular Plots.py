#In this tutorial, we will discuss all about how to create a regular plot in matplotlib

import matplotlib.pyplot as plt
import numpy as np
#Here fill_between() function takes color, axis, alpha as arguments in the below code.

n = 250
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
X
Y = np.sin(3*X)
Y

plt.plot(X, Y+1, color='blue', alpha=1.00)
plt.fill_between(X,3, Y + 1, color='orange', alpha=0.9)

plt.plot(X, Y - 1, color='blue', alpha=1.00)
plt.fill_between(X,-4, Y-1, color='red', alpha=0.9)

plt.show()

#Below are the format string characters which are accepted to control the line style or marker:
#character    	description
#  '-'	         solid line style
#  '--'	      dashed line style
#  '-.'	      dash-dot line style
#  ':'	         dotted line style
#  '.'	         point marker
#  ','	         pixel marker
#  'o'	         circle marker
#  'v'	         triangle_down marker
#  '^'        	triangle_up marker
#  '<'	         triangle_left marker
#  '>'	         triangle_right marker
#  '1'	          tri_down marker
#  '2'	          tri_up marker
#  '3'	         tri_left marker
#  '4'	          tri_right marker
#  's'	          square marker
#  'p'	          pentagon marker
#  '*'	         star marker
#  'h'	          hexagon1 marker
#  'H'        	hexagon2 marker
#  '+'	         plus marker
#  'x'	          x marker
#  'D'	           diamond marker
#  'd'	          thin_diamond marker
#  '|'	          vline marker
#  '_'	          hline marker#


#Below are the supported color abbreviations:

#character   	color
#‘b’	       blue
#‘g’	       green
#‘r’	       red
#‘c’	       cyan
#‘m’	       magenta
#‘y’	       yellow
#‘k’	       black
#‘w’	       white