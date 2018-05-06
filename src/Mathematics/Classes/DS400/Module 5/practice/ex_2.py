# Exercise #2: Generalize the code which was used to determine a limiting
# value at infinity.  Apply to Lial Section 11.1 Example 11.

import numpy
from numpy import sin, arange
import matplotlib.pyplot 
from matplotlib.pyplot import *

# f = ( 12*x**2 - 15*x + 12 ) / ( x**2 + 1 )

# Lial Section 11.1 Example 11
def f(x):
    f = ( 12*x**2 - 15*x + 12 ) / ( x**2 + 1 )
    return f
       
# The next section shows convergence to a limit at infinity.
# The coding shows list manipulations resulting in a plot.
# For simplicity, equal intervals between calculated points will be used.
 
number = 210  # This is the number of points calculated (minus the increment).
increment = 10  # This is the increment between the points.
 
y = []
x = []

# The for loop traverses between 10 and 200 in increments of 10.  
# A range statement is inclusive of the first number and exclusive of the last.

for k in range( increment, number, increment ):
    w = float( k )
    x = x + [ k ]
    y = y + [ f(w) ]
    
print( 'Final value equals' , y[-1] )  #Floating point with 4 decimals.
    
figure()
xlim( 0, number + increment )
ylim( min( y ) - 0.1 , max( y ) + 0.1 )

# The black points were computed.  The yellow point indicates the limit.

plot( x,y, color='r' )
scatter( x,y, color='k', s=30 )
scatter( number, y[-1], c='y', s=40 )

title( 'Example of Convergence to a Limit at Infinity' )
xlabel( 'x-axis' )
ylabel( 'y-axis' )
show()