from sympy import FiniteSet, pi
from fractions import Fraction

s = FiniteSet( 2, 4, 6 )
s

s = FiniteSet( 1, 1.5, Fraction( 1, 5 ) )
s

len( s )

4 in s
1 in s

s = FiniteSet()
s

members = [ 1, 2, 3 ]
s = FiniteSet( *members )
s

values = { 'a': 1, 'b': 2 }
s = sum(**values)
s

a = FiniteSet( 1, 2, 3 )

for member in a:
	print( member )


a = FiniteSet( 3, 4, 5 )
t = FiniteSet( 5, 4, 3 )

s == t

a = FiniteSet( 1 )
t = FiniteSet( 1, 2 )

s.is_subset( t )

t.is_subset( t )

s = FiniteSet( 1, 2, 3 )
ps = s.powerset()
ps

len( ps )

s = FiniteSet( 1 , 2, 3 )
t = FiniteSet( 1, 2, 3 )

s.is_proper_subset( t )

t = FiniteSet( 1, 2, 3, 4 )

t.is_proper_subset( s )
s.is_proper_subset( t )


s = FiniteSet( 1, 2, 3 )
t = FiniteSet( 2, 4, 6 )
s.union( t )

s = FiniteSet( 1, 2, 3 )
t = FiniteSet( 2, 4, 6 )
s.intersect( t )

s = FiniteSet( 1, 2, 3 )
t = FiniteSet( 2, 4, 6 )
u = FiniteSet( 3, 5, 7 )

s.union( t ).union( u )

s.intersect( t ).intersect( u )

s = FiniteSet( 1, 2 )
t = FiniteSet( 3, 4 )

p = s*t
p

for elem in p:
	print( elem )

len( p ) == len( s ) * len( t )

s = FiniteSet( 1, 2 )
p = s ** 3
p

for elem in p:
	print( elem )

def time_period( length ):
	g = 9.8
	T = 2 * pi * ( length ) ** 0.5
	return T

L = FiniteSet( 15, 18, 21, 22.5, 25 )

for l in L:
	t = time_period( l / 100 )
	print( 'Length {0} cm Time Period {1:.3f} s'.format( float( l ), float( t ) ) )