'''
Find the minimum aggregate area for a square and a circle formed by cutting a wire in two pieces.
'''

import math
from sympy import Derivative, symbols, solve, sympify

l = 12

# Side, Circumference

s, c = symbols( 's, c' )
A = ( s / 4 ) ** 2 + ( c**2 / 4 * math.pi )
L = c + s - l
# Solve for c in terms of s
sC = solve( L, s )[ 0 ]
A1 = A.subs( s, sC )

# Single variable, take the derivitave with respect to c.
dA = Derivative( A1, c ).doit()
dA
slns = solve( dA )

slns

