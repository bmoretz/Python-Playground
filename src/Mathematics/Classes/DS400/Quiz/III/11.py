from sympy import *
import matplotlib.pyplot as plt
import numpy as np

g_xlim = [ 0, 5000 ]

def plot_fun( fun, name, col ):
	x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
	y_vals = fun( x_vals )
	plt.plot( x_vals, y_vals, label = name, color = col )

x = symbols( 'x' )

C = 0.15 * x**2 - 0.00004*x**3
R = 1.014 * x**2 - 0.0002*x**3

P = R - C

dP = diff( P, x )
dec = solve( dP )[ 1 ]

print( 'Profit Decreases at {0}'.format( dec ) )

plt.vlines( x = dec, ymax = P.subs( { x : dec } ).evalf(), ymin=0 )

lam_c = lambdify( x, C, np )
plot_fun( lam_c, "C", "R" )

lam_r = lambdify( x, R, np )
plot_fun( lam_r, "R", "B" )

lam_p = lambdify( x, P, np )
plot_fun( lam_p, "P", "G" )


plt.legend()
plt.show()