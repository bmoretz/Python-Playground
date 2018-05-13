# Find the revenue function from the marginal revenue function.

from sympy import solve, symbols, lambdify, diff, integrate, exp, pprint, pretty, simplify, dsolve, Integral, Rational
import matplotlib.pyplot as plt
import numpy as np

# The marginal revenue​ (in thousands of​ dollars) from the sale of x gadgets is given by the following function.
x, u = symbols( 'x u' )
mRev = 4*x*( u ) ** Rational( -3, 2)
fU = x**2 + 28000

# Find the total revenue function if the revenue from 115 gadgets is 33863
gadgets, rev = 120, 34222 / 1000

R = Integral( mRev, x ).doit()

dR = diff( R, x )

dR.subs( { x: gadgets, u: fU } ).evalf()

fun = R - C

fun.subs( { t: 9 } )
