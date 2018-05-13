# An epidemic is growing in a region according to the rate:
# N'(t) = 94t / t^2 + 2

from sympy import *

init_printing( order = 'rev-lex' )

t, C = symbols( 't C' )
dN = 94*t / ( t** 2 + 2 )

time, value, at_time = 0, 35, 21

N = integrate( dN, t )
N0 = N.subs( { t: time } ) + C

vC = round( solve( N0 - value )[ 0 ].evalf(), 3 )

eq = N + vC 

if __name__ == '__main__':
	pprint( eq )
	round( eq.subs( { t : at_time } ).evalf() )