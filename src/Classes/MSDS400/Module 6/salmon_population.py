# The population of salmon next year is given by
# f(S) = Se^r(1 - S / P ),
# where:
# S is this years' salmon population, 
# P is the equilibrium population,
# r is a constant that depends upon how fast the population grows.

# Find f'(S0) and solve the equation f'( S0 ) = 1.
# Graph f'(S0) and y = 1.

# Find the population for which the maximum sustainable harvest occurs if r = 0.4 and P = 850

import math
from sympy import solve, lambdify, symbols, diff, pprint, pretty, simplify, exp
import matplotlib.pyplot as plt
import numpy as np

S = symbols( 'S' )
r, P = 0.4, 850

F = S * exp( r *( 1 - S / P ) )

dF = diff( F, S )

# intersection = round( solve( dF - 1, S )[ 0 ], 3 )

# Graph

domain_end = 20

g_xlim = [ 0, 500 ]
g_ylim = [-5, 10 ]

lam_x = lambdify( S, dF, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_x( x_vals )

plt.plot( x_vals, y_vals, label = '' )
plt.hlines( y = 1, xmin = g_xlim[ 0 ], xmax = g_xlim[ 1 ], color = 'Orange', zorder = 1 )
plt.scatter( intersection, 1, color = 'R' )
plt.show()