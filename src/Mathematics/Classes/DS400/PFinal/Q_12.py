from sympy import symbols, integrate, Rational, lambdify, solve, ln, log, sqrt
import matplotlib.pyplot as plt
import numpy as np

g_xlim = [ 0, 8 ]

x = symbols( 'x' )

def plot_fun_and_der( ax, F, name ):
	x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
	lam_f = lambdify( x, F, np )
	y_vals = lam_f( x_vals )
	ax.plot( x_vals, y_vals, label = name, color = 'B' )
	lam_df = lambdify( x, diff( F, x ), np )
	y_vals = lam_df( x_vals )
	ax.plot( x_vals, y_vals, label = name, color = 'R' )

fig, ( axes ) = plt.subplots( 2, 2 )

f = x**2
plot_fun_and_der( axes[ 0, 0 ], f, str( f ) )

f = 1/x + x
plot_fun_and_der( axes[ 0, 1 ], f, str( f ) )

f = .2*x**3 + 5 
plot_fun_and_der( axes[ 1, 0 ], f, str( f ) )

f = .2*x**3 + 5 
plot_fun_and_der( axes[ 1, 0 ], f, str( f ) )

plt.show()