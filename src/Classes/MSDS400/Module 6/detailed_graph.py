# Graph the​ function, considering the​ domain, critical​ points, symmetry, relative​ extrema, 
# regions where the function is increasing or​ decreasing, inflection​ points, 
# regions where the function is concave upward or concave​ downward, 
# intercepts where​ possible, and asymptotes where applicable.

# f(x) = -4x + 6 / 4x + 3

from sympy import solve, lambdify, symbols, diff, pprint, pretty
import matplotlib.pyplot as plt
import numpy as np

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

domain_end = 20

g_xlim = [-5, 5]
g_ylim = [-5, 70]

x = symbols('x', positive = True ) # 0 <= x
F = ( -4*x + 6 ) / ( 4*x + 3 )

lam_x = lambdify( x, F, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_x( x_vals )

plt.plot( x_vals, y_vals, label = '' )

dF = diff( F, x )

disp_fun( dF )

ddF = diff( F, x, 2 )

disp_fun( ddF )

plt.show()