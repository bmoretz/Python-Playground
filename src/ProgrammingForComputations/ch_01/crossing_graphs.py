import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Consider two functions, 
#	f(x) = x
#   g(x) = x²
#
# Write a program that, by trial and error, finds approximately for which values of x
# the two graphs cross, i.e., f(x) = g(x).
# Do this by considering N equally distributed points in the interval, at each point checking whether:
# |f(x) - g(x)| < ɛ, where ɛ is some small number.
# Let N and ɛ  be user input to the program and let the result be printed to the screen.

# The base case is N = 400 and ɛ = 0.01.

g_xlim = [ -4, 4 ]
g_iter = 1000

def plot_fun( fun, name, col ):
	x_vals = np.linspace( g_xlim[0], g_xlim[1], g_iter, endpoint=True )
	y_vals = fun( x_vals )
	plt.plot( x_vals, y_vals, label = name, color = col )

def f(x):
	return x

def g(x):
	return x**2

plot_fun( f, 'x', 'B' )
plot_fun( g, 'x²', 'G' )

epsilon = 0.0001
N = 40000

v = []

for x in np.linspace( g_xlim[ 0 ], g_xlim[ 1 ], N ):
	delta = abs( f( x ) - g( x ) )

	if delta <= epsilon:
		v.append( x )
		plt.scatter( x, f(x) )

plt.legend()
plt.show()