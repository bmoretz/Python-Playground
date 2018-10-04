# A marshy region used for agricultural drainage has become contaminated with a particular element. 
# It has been determined that flushing the area with clean water will reduce the element for a​ while, but it will then begin to build up again. 
# A biologist has found that the percent of the element in the soil x months after the flushing begins is given by the function below. 
# 
# When will the element be reduced to a​ minimum? What is the minimum​ percent?

from sympy import solve, lambdify, symbols, diff, simplify, pretty, pprint
import matplotlib.pyplot as plt
import numpy as np

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

g_xlim = [ 1, 12 ]
g_ylim = [ -5, 50 ]

x = symbols('x', positive = True ) # 0 <= x
F = ( x**2 + 100 ) / ( 2*x )

lam_x = lambdify( x, F, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_x( x_vals )

plt.plot( x_vals, y_vals, label = '' )

# F'
dF = diff( F, x )

disp_fun( simplify( dF ) )

lam_dx = lambdify( x, dF, np )

dx_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
dy_vals = lam_dx( x_vals )

min = solve( dF, x )[ 0 ]

plt.plot( dx_vals, dy_vals, label = '' )

F.subs( { x: min } ).evalf()

plt.show()