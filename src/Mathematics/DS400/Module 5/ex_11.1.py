import numpy 
from numpy import sin, arange
import matplotlib.pyplot 
from matplotlib.pyplot import *
from sympy import Limit

def g( x ):
    g = x ** 2
    return g

# An example will be used to show right and left convergence to a value.        
# Convergence at x = 0 will be shown graphically using g(x).

n = 5  # This determines the number of values calculated on each side of x=0.

powers = arange( 0, n+1 )

denominator = 2.0 ** powers  # denominator contains exponentiated values of 2.0.

delta = 1           # This is the interval used on either side of the origin.

# The following are values of x and f(x) trending to the limit.
# Delta is being divided by powers of 2 to reduce the distance from the limit.
# The letter "r" denotes from the right, and "l" denotes from the left.

x_r = delta / denominator
y_r = g( x_r )
x_l = -x_r   # The negative sign generates a symmetric point on the left.
y_l = g( x_l )

# The following determines the vertical boundaries of the resulting plot.

ymax = max( abs( y_r ) ) + 0.5
ymin = -ymax

figure()
xlim( -delta - 0.5 , delta + 0.5 )
ylim( ymin, ymax )

# Plotting is being done in layers.  First the line plot then the points.

plot( x_r,y_r, color = 'b' )
plot( x_l,y_l, color = 'r' )

# The black points were computed.  The yellow point marks the limit.

scatter( x_r,y_r, color = 'k', s= 30 )
scatter( x_l,y_l, color = 'k', s= 30 )
scatter( 0.0, g(0.0), c = 'y', s = 40 )

title( 'Example of Convergence to a Functional Value' )
xlabel( 'x-axis' )
ylabel( 'y-axis' )
show()