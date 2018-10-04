from sympy import solve, Limit, lambdify, symbols, diff
import matplotlib.pyplot as plt
import numpy as np

domain_end = 20

g_xlim = [-2, 40]
g_ylim = [-2, 70]

# eq

x = symbols('x', positive = True ) # 0 <= x
R = 11000 - x ** 3 + 42 * x ** 2 + 800 * x # Revenue Cubic

L1 = 950*x + 14200 # Revenue Linear
L2 = -1250*x + 45000 # Linear Constraint

lam_x = lambdify( x, R, np )

lin_x1 = lambdify( x, L1, np )
lin_x2 = lambdify( x, L2, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint = True )
y_vals = lam_x( x_vals )

plt.plot( x_vals, y_vals, label = 'Cubic Revenue', color = 'B' )

# Inflection Point, second derivative, ( Green )

dR = diff( R, x, 2 )
inflection_point = solve( dR, x )[ 0 ]
inflection_value = R.subs( { x: inflection_point } )

# Profit Region
section = np.arange( 0, int( inflection_point ), 1/20.)
plt.fill_between( section, lin_x1(section), color='Green', alpha = .4 )
plt.text( inflection_point / 2, 1500, 'Optimal Region')

# R Inflection Point
plt.hlines( y = inflection_value, xmin = 0, xmax = inflection_point, color = 'Purple', zorder = 1 )
plt.text( 0, inflection_value + 2000, 'Inflection Point')

# Domain End (Black)
plt.vlines( x = domain_end, ymin = 0, ymax = R.subs( { x: domain_end } ), color='Black', zorder=2)
plt.text( domain_end + 1, 1000, 'Domain Bounds' )

bounds = np.arange( domain_end, g_xlim[ 1 ], 1/20., dtype=float)
plt.fill_between( bounds, lam_x(bounds), facecolor='black', alpha = .2 )

# Linear Revenue
lin1_y = lin_x1( x_vals )
plt.plot( x_vals, lin1_y, label = 'Linear Revenue', color = 'Orange' )

# Linear Constraint
lin2_y = lin_x2( x_vals )
plt.plot( x_vals, lin2_y, label = 'Linear Constraint', dashes=[6, 1], color = 'Red' )


plt.xlabel('ROI')
plt.ylabel('Invested $(MM)')
plt.legend()
plt.show()