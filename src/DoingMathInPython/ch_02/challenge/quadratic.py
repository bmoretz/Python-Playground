'''
Quadratic Exploration
'''

from matplotlib import pyplot as plt

import math

# Function: f(x) = x^2 + 2x + 1
def gen_quadratic( x_values ) :
	tmp = []
	for x in x_values:
		# Calculate Quadratic Values
		y = x**2 + 2*x + 1
		tmp.append( [ x, y ] )
	return( tmp )

def plot_points( points, function ):
	plt.plot( [p[0] for p in points], [p[1] for p in points] )
	plt.title( function )

# Assume Values of x
x_values = range( -20, 20, 1 )

vals = gen_quadratic( x_values )
plot_points( vals, 'x^2 + 2x + 1' )

plt.show()