# using GRADIENT DESCENT to find extrema values

'''
Use gradient descent to find the minimum value for a function
'''

import math
from sympy import Derivative, Symbol, sympify
from sympy.core.sympify import SympifyError
from collections import namedtuple

def grad_descent( x0, f1x, v ):
	epsilon = 1e-6
	step_size = 1e-4
	x_old = x0
	x_new = x_old - step_size * f1x.subs( { v: x_old } ).evalf()
	print( x_new )

	while( abs( x_old - x_new ) > epsilon ):
	   x_old = x_new
	   x_new = x_old - step_size * f1x.subs( { v: x_old } ).evalf()
	   print( x_new )

	return round( x_new, 7 )

def find_min( f, v, i ):
	# Calculate the first derivative
	f1x = Derivative( f, v ).doit()
	print( f1x )
	return grad_descent( i, f1x, v )

if __name__ == '__main__':

	try:
		f = sympify( input( 'Enter a function in one variable: ') )
		v = Symbol( input( 'Enter the variable: ' ) )
		i = float( input( 'Enter the initial value: ' ) )
	except SympifyError:
		print( 'Error parsing the function' )
	else:
		x_min = find_min( f, v )
		value = round( f.subs( { v: x_min } ).evalf(), 7 )
		print( 'The global minimum for function {0} is {1} at {2}'.format( f, x_min, value ) )