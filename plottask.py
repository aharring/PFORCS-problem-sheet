# GMIT CyberSecurity : Programming for CyberSecurity, Python
# Lecturer : Andrew Beatty
#
# Problem Sheet Week 8  
#
# Task Requirement :
#       Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
#
# Program Name : plottask.py 
#
# Program Function : 
#       Using imported module numpy the program creates 3 arrays, x is a numpy array in the range of 0-4, y2 is x squared, y3 is x cubed
#       Plot each, with markers, in relation to x using the module matplotlib.
#       Label the axes, make Y horizontal
#       Create a title, a centered legend and a grid. 
#       Display the graph
#       Save the graph image to file
#
#       What I learned :
#          How to manipulate numpy arrays
#          How to plot graphs using matplotlib
#          I've a way to go before the OO version on RealPython makes sense
#
#	References :
#          Weekly recommended reading on w3schools & RealPython
#          https://www.tutorialspoint.com/numpy/numpy_array_from_numerical_ranges.htm - how to define a numpy range
#          stackoverflow - annotate, title spanning 2 lines, superscripts
#
import numpy as np 
import matplotlib.pyplot as mplt 

x = np.arange(4)    # A numpy array in range 0-4. https://www.tutorialspoint.com/numpy/numpy_array_from_numerical_ranges.htm
y2 = x * x
y3 = x * x * x

mplt.plot(x,x, label = "f(x)=x", marker = 'o')
mplt.plot(x, y3, label = "h(x)=$x^3$", marker = 'o')
mplt.plot(x, y2, label= "g(x)=$x^2$", marker = 'o')

mplt.xlabel("X")
mplt.ylabel("Y", rotation='horizontal', ha='right') # So you don't have to turn your head sideways to read 'Y', ha is horizontal alignment

#mplt.annotate("g(x)=$x^3$", xy=(2.7,27)) # This is if you want text to appear along the plotted line
#mplt.annotate("h(x)=$x^2$", xy=(2.7,9))
#mplt.annotate("f(x)=x", xy=(2.7,3))

mplt.title("Y as a function of X, $X^2$, $X^3$ \n GMIT Programming Python Week 08")
mplt.legend(loc='upper center') # Position the legend
mplt.grid()
mplt.show()

mplt.savefig('plottask.png')

