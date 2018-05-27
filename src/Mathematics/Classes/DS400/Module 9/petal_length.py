from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, pprint )
import matplotlib.pyplot as plt
import numpy as np

# The length of a petal on a certain flower varies from 2.25 cm to 6.25 cm and has a probability density function defined by:

x = symbols( 'x' )
F = 1 / ( 2 * sqrt( x ) )

# What does the petal distribution look like?

g_xlim = [ 1, 7 ]
g_ylim = [ -5, 10 ]

lam_p = lambdify( x, F, np )
x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_p( x_vals )
plt.plot( x_vals, y_vals )

x_min, x_max = 2.25, 6.25

plt.vlines( x = x_min, ymin = 0, ymax = F.subs( { x: x_min } ), color = 'Black', zorder = 1 )
plt.vlines( x = x_max, ymin = 0, ymax = F.subs( { x: x_max } ), color = 'Black', zorder = 1 )

# Find the probabilities that the length of a randomly selected petal will be as follows.

# A
# The probability that the length of a randomly selected petal is between 2.5 cm and 2.7 cm is

a, b = 2.5, 2.7
bounds = np.arange( a, b, 1/50., dtype=float)

for n in bounds:
	y = F.subs( { x: n } )
	plt.vlines( x = n, ymin = 0, ymax = y, color = 'Teal', zorder = 1, alpha = .4 )

area = integrate( F, ( x, a, b ) ).evalf()
total_area = integrate( F, ( x, 2.25, 6.25 ) ).evalf()

plt.show()

area_pct = round( ( area / total_area ), 4 )

# B
# Greater than or equal to 2.7 cm

a, b = 2.7, x_max
bounds = np.arange( a, b, 1/50., dtype=float)

for n in bounds:
	y = F.subs( { x: n } )
	plt.vlines( x = n, ymin = 0, ymax = y, color = 'Teal', zorder = 1, alpha = .4 )

area = integrate( F, ( x, a, b ) ).evalf()
total_area = integrate( F, ( x, 2.25, 6.25 ) ).evalf()

plt.show()

area_pct = round( ( area / total_area ), 4 )

# C
# Less than or equal to 2.5 cm

a, b = x_min, 2.5
bounds = np.arange( a, b, 1/50., dtype=float)

for n in bounds:
	y = F.subs( { x: n } )
	plt.vlines( x = n, ymin = 0, ymax = y, color = 'Teal', zorder = 1, alpha = .4 )

area = integrate( F, ( x, a, b ) ).evalf()
total_area = integrate( F, ( x, 2.25, 6.25 ) ).evalf()

plt.show()

area_pct = round( ( area / total_area ), 4 )