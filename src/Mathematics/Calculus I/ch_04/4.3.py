from math import sqrt, exp, log, sin, pi
from sympy import Symbol, Limit, Derivative, solve, sympify, S, simplify, lambdify, pprint, init_printing, symbols
from fractions import Fraction

init_printing( order = 'rev-lex', use_unicode = True )

# 4.3.2

# Find the derivitave: f(x) =(2x)^3 * (3x)^2 

Fx = ( 2*x )**3 * ( 3*x )**2
x = Symbol( 'x' )
Derivative( Fx, x ).doit()

# 4.3.3

# Find the derivitave: f(x) = 7 * [ x ^ 7/3 + 11/7*x^7/5 + 13x^7/7 ] ^ 4/3

Fx = 7 * ( x ** 7/3 + 11/7*x**7/5 + 13*x**7/7 ) ** 4/3
x = Symbol( 'x' )
Derivative( Fx, x ).doit()

# 4.3.9

# A particle's position is given by the function: x(t) = ( 4 - t ) ^ 3.
# What is the value of dx/dt when t = 3 ?

Ft = ( 4 - t ) ** 3
t = Symbol( 't' )
Dt = Derivative( Ft, t ).doit()
pprint( Dt )
Dt.subs( { t: 3 } )