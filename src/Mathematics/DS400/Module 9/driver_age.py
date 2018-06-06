from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, pprint )
import matplotlib.pyplot as plt
import numpy as np

# If the age of a randomly selected driver in a fatal car crash is a random variable with a probability density function given by

x = symbols( 'x' )
F = 0.01912 * exp( -0.00321 * x )

# What does the petal distribution look like?

g_xlim = [ -1, 90 ]

lam_p = lambdify( x, F, np )
x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_p( x_vals )
plt.plot( x_vals, y_vals )

x_min, x_max = 18, 79

plt.hlines( y = 0, xmin = g_xlim[0], xmax = g_xlim[1], color = 'Black', zorder = 1 )

plt.vlines( x = x_min, ymin = 0, ymax = F.subs( { x: x_min } ), color = 'Black', zorder = 1 )
plt.vlines( x = x_max, ymin = 0, ymax = F.subs( { x: x_max } ), color = 'Red', zorder = 1 )

# The probability that the​ driver's age is between 24 and 45 is

a, b = 24, 45
bounds = np.arange( a, b, 1/25., dtype=float)

for n in bounds:
	y = F.subs( { x: n } )
	plt.vlines( x = n, ymin = 0, ymax = y, color = 'Teal', zorder = 1, alpha = .4 )

area = integrate( F, ( x, a, b ) ).evalf()
total_area = integrate( F, ( x, x_min, x_max ) ).evalf()

area_pct = round( ( area / total_area ), 2 )

plt.title( 'Area: {0}'.format( area_pct ) )
plt.show()

# The probability that the​ driver's age is greater than or equal to 33

a, b = 32, x_max
bounds = np.arange( a, b, 1/25., dtype=float)

for n in bounds:
	y = F.subs( { x: n } )
	plt.vlines( x = n, ymin = 0, ymax = y, color = 'Teal', zorder = 1, alpha = .4 )

area = integrate( F, ( x, a, b ) ).evalf()
total_area = integrate( F, ( x, x_min, x_max ) ).evalf()

area_pct = round( ( area / total_area ), 2 )

plt.title( 'Area: {0}'.format( area_pct ) )
plt.show()

# The probability that the driver is less than or equal to 28.

a, b = x_min, 21
bounds = np.arange( a, b, 1/25., dtype=float)

for n in bounds:
	y = F.subs( { x: n } )
	plt.vlines( x = n, ymin = 0, ymax = y, color = 'Teal', zorder = 1, alpha = .4 )

area = integrate( F, ( x, a, b ) ).evalf()
total_area = integrate( F, ( x, x_min, x_max ) ).evalf()

area_pct = round( ( area / total_area ), 2 )

plt.title( 'Area: {0}'.format( area_pct ) )
plt.show()

# Find the cumulative distribution function for this random variable.
a, b = x_min, x
cdf = integrate( F, ( x, a, b ) )

pprint( cdf )

round( 5.95638629283489, 5 )

#  Use the answer to part D to find the probability that a randomly selected driver in a fatal crash is at most 24 years old.

ans = cdf.subs( { x: 23 } ).evalf()
round( ans, 2 )