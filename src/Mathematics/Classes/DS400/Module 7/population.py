# A population grows at a rate
# P'(t) = 400te^( -t^2 / 7 )

from sympy import *

init_printing( order = 'rev-lex' )

t, C = symbols( 't C' )
dP = 400*t*exp( -t**2 / 7 )

time, value, at_time = 0, 4000, 6

P = integrate( dP, t )
P0 = P.subs( { t: time } ) + C

vC = round( solve( N0 - value )[ 0 ].evalf(), 3 )

eq = P + vC 

if __name__ == '__main__':
	pprint( eq )
	round( eq.subs( { t : at_time } ).evalf() )