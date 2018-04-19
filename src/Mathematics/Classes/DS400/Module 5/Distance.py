# The distance of a particle from some fixed point is given by the following function.

from sympy import symbols, Limit, Derivative, Integral


def rate_of_change( f, a, b ):
	return ( f.subs( { t: b } ) - f.subs( { t: a } ) ) \
	/ ( b - a )

t = symbols( 't' )
sT = t**2 + 3*t - 2

a = 5
b = 7

rate_of_change( sT, a, b )

d = Derivative( 