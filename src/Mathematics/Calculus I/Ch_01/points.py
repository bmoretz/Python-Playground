from fractions import Fraction

class Point:
	def __init__( self, x = 0, y = 0 ):
		self.x = x
		self.y = y

def slope_coord( x1, y1, x2, y2 ):
	m = ( y2 - y1 ) / ( x2 - x1 )
	return m

def slope_point( p1, p2 ):
	return slope_coord( p1.x, p1.y, p2.x, p2.y )

def distance( p1, p2 ):
	return ( ( p2.x - p1.x )**2 + ( p2.y - p1.y ) ** 2 ) ** .5

def print_fraction( desc, d ):
	print( desc + str( Fraction( m ).limit_denominator() ) )

p1 = Point( -2, 3 )
p2 = Point( 4, 11 )

m = slope_point( p1, p2 )
d = distance( p1, p2 )

d
d ** 2

print_fraction( "slope: ", m )

