# Find the minimum value of the average cost for the given cost function on the given intervals.
# C(x) = x**3 + 29*x + 432

from sympy import solve, lambdify, symbols, diff, pprint, pretty
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x', positive = True ) # 0 <= x
C = x**3 + 29*x + 432
avgC = C / x

domain_end = 20

g_xlim = [ 10, 20 ]
g_ylim = [-5, 70]

lam_x = lambdify( x, avgC, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_x( x_vals )

plt.plot( x_vals, y_vals, label = '' )

# The minimum value of the average cost over the interval 1 <= x <=10

daC = diff( avgC, x, 1 )

min = solve( daC, x )[ 0 ]

# Global Min
avgC.subs( { x: min } )

# Plotted Area Min
y_vals.min()

plt.show()