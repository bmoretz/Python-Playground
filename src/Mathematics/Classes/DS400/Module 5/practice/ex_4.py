# Exercise #2: Refer to Lial 11.1 Example 1.  This was used in Session 6 
# Module1. The solution code is presented in the answer sheet.  Modify the code
# so that the tangent line at x=2 appears on the preceeding plot.  This 
# necessitates determining the linear equation for the tangent line using
# y=mx+b and writing the statements to plot this line on the existing plot.
# Use arange().

import numpy 
from numpy import arange, cos
import matplotlib.pyplot 
from matplotlib.pyplot import *

# Define a function for demonstration.  This function may be changed.

def f(x):
    f = cos(x)    
    return f

def der( x, delta ):
    delta = float( delta )
    if delta < ( 0.0000001 ):
        print ('Value chosen for delta is too small.')
        return 1/delta
    else:
        slope = (f(x + delta) - f(x))/delta
        return slope

point = 1.0  #This is a point at which a derivative will be calculated.
# The following statements initialize variables for computation.

limit = der( point, 0.000001 )

# The next section will show the tangent line at the point x=1.0.
# We are using the equation for a straight line y=mx+b where the slope is
# y[-1] from above and the point given above is x=1.0.  We are only going 
# to plot this tangent line over a limited distance given by w defined below.

# Calculate values for the tangent.
w = arange( point - 1.0, point + 1.1, 0.1 )
t = f( point ) + limit * ( w-point )

# Now we are going to plot the original function over a wider range.
# Define a domain for the function.
domain = 3.14

# Calculate values for the function on both sides of x=1.0.
u = arange( point-domain, point+domain + 0.1, 0.1 )
z = f(u)

# This allows us to plot in layers showing the tangent and the function.
# The scatter command allows a single point to be plotted.
figure()
xlim( point-domain -.1, point+domain + 0.1 )
ylim( max(z)+.5, min(z)-.5 )

plot( w, t, c='r')                        # This plots the tangent line.
plot( u, z, c='b' )                        # This plots the curve itself.
scatter( point, f(point), c='g', s=40)     # This is the point of contact.
xlabel('x-axis')
ylabel('y-axis')
title('Plot showing function and tangent at a point')
show()