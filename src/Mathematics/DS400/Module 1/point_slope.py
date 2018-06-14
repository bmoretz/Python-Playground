import math
from sympy import symbols, solve, pprint

p1 = [ 0, 0 ]
p2 = [ 6, 504 ]
m = None

m1 = ( p2[ 1 ] - p1[ 1 ] )
m2 = ( p2[ 0 ] - p1[ 0 ] )

def line( x0, y0, m ):
	x, y = symbols( 'x, y' )
	eq = m * ( x - x0 ) + y0 - y
	
	sln = solve( eq, y )

	return 'y = {0}'.format( sln[0] )

if __name__ == '__main__':

	if m != 0 and m != None:
		l = line( p1[ 0 ], p1[ 1 ], m )
		pprint( l )
	elif m == 0:
		print( "y = {0}".format( p1[ 1 ] ) )
	elif m2 == 0:
		print( "x = {0}".format( p1[ 0 ] ) )
	else:
		m = m1 / m2
		line( p1[ 1 ], p2[ 1 ], m )