import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import arange

# Feasible region, Lial S 3.1, E 5

x= arange(-2,6.1,0.1)
y= -1.0 + x/4.0
figure()
xlim(-1,6)  # Plot limits must be set for the graph.
xlabel('x-axis')  # Plot axes must be specified.  Setting the grid is optional. 
ylabel('y-axis')
hlines(0,-2,6,color='r')
vlines(0,-2,6,color='r')
grid(True)
plot(x,y)
print('Data points are plotted using variable z to define a boundary for the\
filled area.  z is a list with the same dimension as x and y.  It provides a\
lower boundary for the plot so that the region can be filled.')
z = -2.0 + 0.0*x
plot(x,z)
print("Region is filled to show the region.  fill_between() will fill between two\
lines.  It is difficult to use with irregular polygons.")
fill_between(x,y,z, color= 'b')
title ('Shaded Area Shows the Linear Inequality x-4y > 4')
show()

figure()
x= arange(-3,10.1,0.1)
y= arange(-3,10.1,0.1)
y1= 0.4*x-2.0
y2= 4.0-0.5*x

# Feasible region, Lial S 3.1, E 5
xlim(-3,10)
ylim(-3,10)

hlines(0,-3,10,color='k')
vlines(0,-3,10,color='k')
grid(True)

xlabel('x-axis')
ylabel('y-axis')
title ('Shaded Area Shows the Feasible Region')

plot(x,y1,color='b')
plot(x,y2,color='r')
legend(['2x-5y=10','x+2y=8'])
print("The simplest approach for filling a polygon is to locate the\
corner points. Matplotlib will fill within these points.")

x= [0.0, 0.0, 6.67,5.0]
y= [0.0, 4.0, .67, 0.0]

fill(x,y)
show()