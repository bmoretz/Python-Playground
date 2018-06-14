# A local club is arranging a charter flight to Hawaii.

from sympy import *
import matplotlib.pyplot as plt
import numpy as np

def plot_fun( fun, name ):
	x_vals = np.linspace( g_xlim[0], g_xlim[1], 100, endpoint=True )
	y_vals = fun( x_vals )
	plt.plot( x_vals, y_vals, label = name )

g_xlim = [ 0, 200 ]

#  The cost of the trip is ​$589 each for 83 ​passengers, 
#  with a refund of​ $5 per passenger for each passenger in excess of 83.

x = symbols( 'x' )

C = (589*83) - 5*x

lam_c = lambdify( x, C, np )
plot_fun( lam_c, 'C' )

dC = diff( C, x, 2 )
solve( dC, x )

plt.legend()
plt.show()

round( solve( C, x )[ 0 ].evalf() )

C.subs( { x: 118 } )