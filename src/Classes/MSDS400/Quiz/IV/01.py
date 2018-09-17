from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, pprint, Integral )
import matplotlib.pyplot as plt
import numpy as np

# The number of​ bachelor's degrees conferred has been increasing steadily in recent decades.
# The rate of change of the number of​ bachelor's degrees​ (in thousands) can be approximated by the following function where t is the number of years since 1970.

t = symbols( 't' )
dB = 0.0651 * t**2 - 1.939 *t + 16.31

# Divide by 1000
y_min = 833300 / 1000

B = Integral( dB, t ).doit() + y_min

B.subs( { t: 0 } ) == y_min # Verify

# Find Upper B(t)​, given that about 819,900 degrees were conferred in 1970 ​(t=​0).
pprint( B )

# Use the formula from part a. to project the number of​ bachelor's degrees that will be conferred in 2010, t = 40
year_tofind = 40

deg_2010 = B.subs( { t: year_tofind } )
degrees = round( deg_2010 * 1000 )
degrees

# What does the degree distribution look like?

g_xlim = [ 0, 50 ]

lam_p = lambdify( t, B, np )
x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint = True )
y_vals = lam_p( x_vals )
plt.plot( x_vals, y_vals )
x_min, x_max = 0, year_tofind

plt.vlines( x = x_min, ymin = y_min, ymax = B.subs( { t: x_min } ), color = 'Black', zorder = 1 )
plt.vlines( x = x_max, ymin = y_min, ymax = B.subs( { t: x_max } ), color = 'Red', zorder = 1 )
plt.text( x = x_max, y= deg_2010, s = str( degrees ) )


plt.title( str( B ) )
plt.show()