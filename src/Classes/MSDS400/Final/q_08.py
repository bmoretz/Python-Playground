from sympy import symbols, solve, diff, pprint, integrate, ln, lambdify
import matplotlib.pyplot as plt
import numpy as np
import math

# An oil tanker is leaking oil at a rate given in barrels per hour by the function shown​ below, 
# where t is the time in hours after the tanker hits a hidden rock

t = symbols( 't' )
dL = 76 * ln( t + 1 ) / ( t + 1 )

# Time in hours, first day
a, b = 0, 24
day1 = integrate( dL, ( t, a, b ) ).evalf()

round( day1 ) # Round to three decimal places as​ needed.

solve( integrate( dL, t ), t )

# Time in hours, first day
a, b = 24, 48
day2 = integrate( dL, ( t, a, b ) ).evalf()

round( day2 ) # Round to three decimal places as​ needed.

# Time in hours, first day
a, b = 10000 * 24, 10001 * 24
day11 = integrate( dL, ( t, a, b ) ).evalf()

round( day11 ) # Round to three decimal places as​ needed.

# What is the leak doing?
g_xlim = [ 1, 100 ]
g_ylim = [ -5, 15 ]

lam_l = lambdify( t, integrate( dL, t ), np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_l( x_vals )
plt.plot( x_vals, y_vals )
plt.show()