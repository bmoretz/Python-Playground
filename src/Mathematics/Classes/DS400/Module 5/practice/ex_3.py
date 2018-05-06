# Exercise #1:  Refer to Lial Section 11.3 Examples 3-5.  Using the function 
# der() as defined, calculate approximate slopes for the functions given in 
# Lial Section 11.3 Examples 3(b), 4(c), & 5.  Use a small value for delta and 
# evaluate der() at the points used in the examples. Round to 4 decimal places.

import numpy 
from numpy import arange, cos
import matplotlib.pyplot 
from matplotlib.pyplot import *

# A general function for calculating the slope between two points: x and 
# x+delta.  See Lial Section 11.3 dealing with instantaneous rates of change.

def der( x, delta ):
    delta = float( delta )
    if delta < (0.0000001):
        print ('Value chosen for delta is too small.')
        return 1 / delta
    else:
        slope = ( f (x + delta) - f(x) ) / delta
        return slope

# Define a function for demonstration.  This function may be changed.

def f(x):
    f = cos( x )
    return f
    
point = 1.0  #This is a point at which a derivative will be calculated.
# The following statements initialize variables for computation.

number = 510
increment = 10
y = []
x = []

# What follows shows calculations and list manipulations. Recall that a range
# statement is inclusive of the first number and exclusive of the last.  In this
# example we are incrementing by units of 10 from 1 to 500.  We are reducing
# the distance between x=1.0 and x=1.0+delta by reducing delta.  The slopes
# being calculated are stored in the list y.

for k in range( increment, number, increment ):
    delta = 1.0/(k+1)
    d = der(point,delta)
    x = x + [k]
    y = y + [d]
    max_x = k + increment

limit = der( point,0.000001 )    
print( 'Final value equals', limit )

# The plot shows convergence of the slopes to the instantaneous rate of change. 
# Black dots mark computed slopes as delta was reduced.  The x-axis is plotted
# using values of k from the range statement in the for loop.

figure()

xlim( 0, max_x+50 )
ylim( min( y ) -0.05, max( y ) + 0.05)

scatter( 540, limit, color='g', s=40, label = 'limiting slope')
legend( ( 'limiting slope' ), loc = 'best' )
scatter( x, y, c='k', s=20 )

title ('Example of Convergence to Instanteous Rate of Change')
xlabel('x-axis')
ylabel('y-axis')
ylabel('y-axis')
plot( x,y )
show()
