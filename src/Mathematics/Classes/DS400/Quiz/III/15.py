from sympy import *
import matplotlib.pyplot as plt
import numpy as np
# For a certain​ automobile, Upper M(x), represents the miles per gallon obtained at a speed of x miles per hour.

x = symbols( 'x' )
M = -.015 * x**2 + 1.38*x - 7.3 # 30 <= x <= 60
#M = -0.015 * x**2 + 1.44*x - 7.1 # 30 <= x <= 60
dM = diff( M, x )

critical_values = solve( dM, x )

g_xlim = [ 30, 60 ]
lam_m = lambdify( x, M, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 10000, endpoint=True )
y_vals = lam_m( x_vals )

min_val = g_xlim[ 0 ]
min = M.subs( { x: min_val } )
# (Type an integer or decimal rounded to the nearest thousandth as​ needed.)
print( 'Absolute Minimum MPG is {0} at {1} mph'.format( round( min, 3 ), round( min_val ) ) )

max_val = critical_values[ 0 ]
max = M.subs( { x: max_val } )
# (Type an integer or decimal rounded to the nearest thousandth as​ needed.)
print( 'Absolute Maximum MPG is {0} at {1} mph'.format( round( max, 3 ), round( max_val ) ) )

plt.plot( x_vals, y_vals, label = '' )
plt.show()