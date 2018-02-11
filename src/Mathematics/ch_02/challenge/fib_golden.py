'''
Fibonacci Sequence & Golden Ratio
'''


from matplotlib import pyplot as plt

import math

def fibo( n ):
	if n == 1:
		return [1]
	if n == 2:
		return [1, 1 ]

	a = 1
	b = 1

	series = [ a, b ]

	for i in range( n ):
		c = a + b
		series.append( c )
		a = b
		b = c

	return series

def plot_points( x_vals, y_vals ):
	plt.plot( x_vals, y_vals )
	plt.title( 'Ration betwen consecutive Fibonacci numbers' )

fib = fibo( 100 )

x_vals = range( 2, len(fib) + 1, 1 )

plot_points( x_vals, [ fib[ x - 1 ] / fib[ x - 2 ]  for x in x_vals ] )

plt.show()