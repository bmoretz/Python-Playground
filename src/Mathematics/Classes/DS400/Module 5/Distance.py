# The distance of a particle from some fixed point is given by the following function.

from sympy import symbols, Limit, Derivative, Integral

def rate_of_change( f, a, b ):
	return ( f.subs( { t: b } ) - f.subs( { t: a } ) ) \
	/ ( b - a )

t,h = symbols( 't,h' )
sT = t**2 + 3*t - 2

a = 5
b = 5

if a == b:
	l = Limit( sT, t, ( a + h ) ).doit()
	d = Derivative( l, h ).doit()
	d.subs( { h: 0 } )
else:
	rate_of_change( sT, a, b )