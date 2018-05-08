# The total profit​ P(x) (in thousands of​ dollars) from a sale of x thousand units of a new product is given by:
# P(x) = ln( -x**3 + 3*x**2 + 105*x + 1 )

from sympy import solve, Limit, lambdify, symbols, diff, ln
import matplotlib.pyplot as plt
import numpy as np

init_printing()

g_xlim = [ -15, 15 ]
g_ylim = [ -7, 7 ]

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

x = symbols( 'x' )

P = ln( -x**3 + 3*x**2 + 105*x + 1 )
dP = diff( P, x )

lam_x = lambdify( x, P, modules=['numpy'] )

x_vals = np.linspace( -10, 10, 1000, endpoint = True )
y_vals = lam_x( x_vals )

plt.plot( x_vals, y_vals )
plt.xlim( g_xlim )
plt.ylim( g_ylim )
plt.ylabel( "Profit" )
plt.show()

round( P.subs( { x: 7 } ).evalf() * 1000, 2 )