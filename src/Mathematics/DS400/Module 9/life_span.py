from sympy import ( symbols, solve, diff, integrate, exp, lambdify, pprint )
import matplotlib.pyplot as plt
import numpy as np

# The life​ (in months) of a certain electronic computer part has a probability density function defined by F,
# Find the probability that a randomly selected component will last the following lengths of time.

x = symbols( 'x' )
F = .5 * exp( -x / 2 )

# What does the life-span look like?
g_xlim = [ 1, 20 ]
g_ylim = [ -5, 15 ]

lam_p = lambdify( x, F, np )
x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_p( x_vals )
plt.plot( x_vals, y_vals )

# Probability it will last 8 months?

a, b = 4, 8
bounds = np.arange( a, b, 1/50., dtype=float)

for n in bounds:
	y = F.subs( { x: n } )
	plt.vlines( x = n, ymin = 0, ymax = y, color = 'Teal', zorder = 1, alpha = .4 )

area = integrate( F, ( x, a, b ) ).evalf()

total_area = integrate( F, ( x, 0, 100 ) ).evalf()

area_pct = round( ( area / total_area ), 4 )
plt.text( 2 , .1, 'Area: {0}%'.format( area_pct ) )

plt.show()

# Find the cumulative distribution function for this random variable.
a, b = 0, x
cdf = integrate( F, ( x, a, b ) )

pprint( cdf )

#  Use the answer to part C to find the probability that a randomly selected component will last at most 6 months.

ans = cdf.subs( { x: 6 } ).evalf()
round( ans, 4 )