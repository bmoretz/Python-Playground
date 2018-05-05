# Consider a child waiting at a street corner for a gap in traffic that is large enough so that he can safely cross the street.
# A mathematical model for traffic shows that if the expected waiting time for the child is to be at most 1​ minute, then the maximum traffic​ flow, in cars per​ hour, is given by
# f(x) = 29,403( 2.335 - log( x ) ) / x, where x is the width of the street in feet.

import mpmath
from sympy import *
from fractions import Fraction

init_printing()

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

x = symbols( 'x' )

fX = 29403 * ( 2.335 - log( x, 10 ) )  / x
dX = diff( fX, x )

simplify( dX )

# Find the maximum traffic flow and the rate of change of the maximum traffic flow with respect to street width for the street width of 35 feet.
# (Do not round until the final answer. Then round to the nearest integer as​ needed.)
round( fX.subs( { x: 35 } ).evalf(), 0 )

# The rate of change of the maximum traffic flow is about X vehicles per hour per foot.
# ​(Do not round until the final answer. Then round to the nearest tenth as​ needed.)
round( dX.subs( { x: 35 } ).evalf(), 1 )


# Find the maximum traffic flow and the rate of change of the maximum traffic flow with respect to street width for the street width of 54 feet.
# (Do not round until the final answer. Then round to the nearest integer as​ needed.)
round( fX.subs( { x: 54 } ).evalf(), 0 )

# The rate of change of the maximum traffic flow is about X vehicles per hour per foot.
# ​(Do not round until the final answer. Then round to the nearest tenth as​ needed.)
round( dX.subs( { x: 54 } ).evalf(), 1 )