'''
Construct a box with the maximum volume from a solid piece of material.
'''

import math
from sympy import Derivative, Symbol, solve

def box_volume( w, h ):
	s = Symbol( 's' )
	# v = b * * w * h
	V = ( h - 2*s ) * ( w - 2*s ) * s
	dV = Derivative( V, s ).doit()

	canidates = solve( dV )

	# Eliminate impossible Values
	for c in canidates:
		l = 2 * c.evalf()

		if( l > w or l > h ):
			canidates.remove( c )
	
	max_vol = 0

	if( len( canidates ) != 1 ):
		print( 'Invalid number of solutions.' )
	else:
		s0 = canidates[ 0 ].evalf()
		max_vol = V.subs( { s: s0 } )

	return max_vol

if __name__ == '__main__':

	try:
		w = float( input( 'Enter the width of the material piece: ') )
		h = float( input( 'Enter the height of the material piece: ') )
	except ValueError:
		print( 'Error parsing values' )
	else:
		print( 'material dimentions: {0} x {1}'.format( w, h ) )
		print( 'Maximum box volume: {0}'.format( box_volume( w, h ) ) )