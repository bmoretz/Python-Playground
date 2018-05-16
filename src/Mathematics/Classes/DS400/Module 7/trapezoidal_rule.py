from sympy import *
import matplotlib.pyplot as plt
import numpy as np
# Find the area under the semicircle

x = symbols( 'x', positive = True )
S = sqrt( x**2 + 1 )

a, b, n = 0, 2, 4

def trapezoidal_rule( f, a, b, n ):
	area = 0

	steps = np.linspace( a, b, n + 1, endpoint = True )

	for i in range( 0, n + 1 ):

		v = f.subs( { x: steps[ i ] } )

		if i == 1 or i == n:
			area += .5 * v
		else:
			area += v
	
	return area * ( b - a ) / n


area = trapezoidal_rule( S, a, b, n )

g_xlim = [ -5, 5 ]

lam_s = lambdify( x, S, np )
x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_s( x_vals )

plt.title( 'Trapezoidal Rule Area: {0}'.format( round( area, 3 ) ) )
plt.plot( x_vals, y_vals )
plt.show()
