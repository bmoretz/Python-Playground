# The total profit​ P(x) (in thousands of​ dollars) from a sale of x thousand units of a new product is given by:
# P(x) = ln( -x**3 + 3*x**2 + 105*x + 1 )

from sympy import solve, Limit, lambdify, symbols, diff, ln
import matplotlib.pyplot as plt
import numpy as np

g_xlim = [ 0, 10 ]
g_ylim = [ 0, 7 ]

x = symbols( 'x' )

P = ln( -x**3 + 3*x**2 + 105*x + 1 )
dP = diff( P, x )

lam_x = lambdify( x, P, modules=['numpy'] )

x_vals = np.linspace( g_xlim[ 0 ], g_xlim[ 1 ], 1000, endpoint = True )
y_vals = lam_x( x_vals )

plt.plot( x_vals, y_vals )
plt.xlim( g_xlim )
plt.ylim( g_ylim )
plt.xlabel( 'Units Produced' )
plt.ylabel( "Profit" )
plt.show()