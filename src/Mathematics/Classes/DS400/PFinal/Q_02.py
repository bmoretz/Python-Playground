# Northwest Molded molds plastic handles which cost ​$1.00 per handle to mold. The fixed cost to run the molding machine is $ 4,467 per week. 
# If the company sells the handles for ​$4.00 ​each, how many handles must be molded weekly to break​ even?

from sympy import solve, lambdify, symbols, diff, pprint, pretty
import matplotlib.pyplot as plt
import numpy as np

x = symbols( 'x', positive = True ) # 0 <= x
C = x + 4467
R = 4*x

P = R - C

break_even = solve( P, x )[ 0 ]
domain_end = int( break_even + ( break_even * .1 ) )

g_xlim = [ 0, domain_end ]
g_ylim = [ 0, 70 ]

lam_x = lambdify( x, P, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_x( x_vals )

# Cost Function
plt.plot( x_vals, y_vals, label = 'Cost Function' )

plt.vlines( x = break_even, ymin = min( y_vals ), ymax = P.subs( { x: break_even } ), color = 'Red', zorder = 1, label = 'Break Even: {0:,}'.format( int(break_even) )  )

plt.legend()
plt.show()
