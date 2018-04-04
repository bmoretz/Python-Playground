import math
from sympy import Symbol, Limit, Derivative, solve, sympify, S, simplify, lambdify, pprint, init_printing, symbols
from fractions import Fraction
import numpy as np

init_printing( order = 'rev-lex', use_unicode = True )

# 5.2.1

# Simplify: N ^ A * N ^ B
A,B,N = symbols( 'A,B,N' )
simplify( N ** A * N**B )

# 5.2.3

# Find the derivative: f(x) = 2x^2 + 2e^x
x = Symbol( 'x' )
Fx = 2*x**2 + 2*math.e**x
Derivative( Fx, x ).doit()

# 5.2.4

# Given f(x) = 3 ^ x, evaluate f(4)

3 ** 4

# 5.2.5

# Given f(x) = e^2x, evaluate f(3)

math.e ** (2*3)

# 5.2.9

# Find the derivative: f(x) = 2^x
Fx = 2 ** x
x = Symbol( 'x' )
Derivative( Fx, x ).doit()