# Find the revenue function from the marginal revenue function.

import math
from sympy import solve, symbols, lambdify, diff, integrate, exp, pprint, pretty, simplify, Rational
import matplotlib.pyplot as plt
import numpy as np

# The marginal revenue​ (in thousands of​ dollars) from the sale of x gadgets is given by the following function.
x, C = symbols( 'x C' )
mRev = 4*x*( x**2 + 26000 ) ** ( Rational( -2, 3 ) )

pprint( mRev )

# Find the total revenue function if the revenue from 115 gadgets is 33863
gadgets, rev = 115, 33863 / 1000

R = integrate( mRev, x )
F = solve( R - rev + C, C )

fR = R + round( F[ 0 ].subs( { x: gadgets } ) ) 

solve( fR - 45 )[ 0 ].evalf()