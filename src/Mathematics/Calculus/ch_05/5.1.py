import math
from sympy import Symbol, Limit, Derivative, solve, sympify, S, simplify, lambdify, pprint, init_printing, symbols
from fractions import Fraction
import numpy as np

init_printing( order = 'rev-lex', use_unicode = True )

# 5.1.1

# Find the derivative:
# f(t) = tan^3t

t = Symbol( 't' )
Ft = np.sin( t ) ** 3

Derivative( sin( t ), t )