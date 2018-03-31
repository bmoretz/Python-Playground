'''
Find the minimum aggregate area for a square and a circle formed by cutting a wire in two pieces.
'''

import math
from sympy import Derivative, symbols, solve, sympify
from collections import namedtuple

Pieces = namedtuple( 'Pieces', [ 'circumference', 'side'] )

def cut_wire( l ):
	# Side, Circumference
	s, c = symbols( 's, c' )
	# V = s^2 ( square ) + pi * ( c / 2pi )^2
	A = ( s / 4 ) ** 2 + c**2 / ( 4 * math.pi )
	
	# c + s = l
	L = c + s - l

	# Solve for c in terms of s
	sC = solve( L, s )[ 0 ]
	
	# A1 = area in terms of a single variable
	A1 = A.subs( s, sC )
	
	# Now single variable, take The derivitave with respect to c.
	dA = Derivative( A1, c ).doit()
	slns = solve( dA )

	min_c = slns[ 0 ]
	min_s = l - min_c

	return Pieces( circumference = min_c, side = min_s )

def area_sqare( s ):
	return s**2

def area_circle( c ):
	return c**2 / ( 4 * math.pi )

if __name__ == '__main__':

	try:
		l = float( input( 'Enter the length of the wire to cut: ') )
	except ValueError:
		print( 'Error parsing values' )
	else:
		print( 'wire length: {0}\n'.format( l ) )

		pieces = cut_wire( l )
		area_circle = area_circle( pieces.circumference )
		area_sqare = area_sqare( pieces.side )
		
		print( 'Mimimum Area: {0}'.format( area_circle + area_sqare ) )
		print( 'Circle Area: {0}'.format( area_circle ) )
		print( 'Square Area: {0}'.format( area_sqare ) )