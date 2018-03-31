'''
Construct a can with the maximum volume from a solid piece of material.
'''

import math
from sympy import Derivative, symbols, solve
from collections import namedtuple

Dimension = namedtuple( 'Dimension', [ 'width', 'height', 'volume'] )

def can_volume( area ):

	r,h = symbols( 'r,h' )
	# v = πr²h
	surf_area = 2*math.pi*r**2 + 2*math.pi*r*h
	# Solve surf_area for h, reduce to single variable.
	Ah = solve( surf_area - area, h )[ 0 ]

	V = math.pi * r**2 * h
	V1 = V.subs( h, Ah )

	# Derivative of volume with respect to the radius.
	dV = Derivative( V1, r ).doit()

	canidates = solve( dV )

	# Eliminate impossible Values
	for c in canidates:
		if( c <= 0 ):
			canidates.remove( c )
	
	h0 = 0

	if( len( canidates ) != 1 ):
		print( 'Invalid number of solutions.' )
	else:
		r0 = canidates[ 0 ].evalf()
		h0 = Ah.subs( { r: r0 } )

	return Dimension( width = r0, height = h0, volume = cyl_volume( r0, h0 ) )

def cyl_volume( r, h ):
	return math.pi * r**2 * h

if __name__ == '__main__':

	try:
		area = float( input( 'Enter the area of the material piece: ') )
	except ValueError:
		print( 'Error parsing values' )
	else:
		dim = can_volume( area )
		print( 'Maximum can volume: {0}'.format( dim.volume ) )
		print( 'with dimentions: {0} x {1}'.format( dim.width, dim.height ) )