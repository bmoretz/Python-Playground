'''
Find the area between two curves.
'''

import math
from sympy import Integral, Symbol, sympify
from sympy.core.sympify import SympifyError
from collections import namedtuple

def area_curves( f1, f2, lower, upper ):
	x = Symbol( 'x' )
	return Integral( f1x - f2x, ( x, lower, upper ) ).doit()

if __name__ == '__main__':

	try:
		f1 = sympify( input( 'Enter a function in one variable (upper): ') )
		f2 = sympify( input( 'Enter a function in one variable (lower): ') )
		lower = float( input( 'Enter the lower bound: ' )	)
		upper = float( input( 'Enter the upper bound: ' ) )
	except SympifyError:
		print( 'Error parsing the function' )
	else:
		area = area_curves( f1, f2, lower, upper )
		print( 'The area between the curves formed by in intersection of {0} and {1} bewtwen {2} and {3} is {4}'.format( f1, f2, lower, upper, area ) )