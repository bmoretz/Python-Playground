from math import sqrt, exp, log, sin, pi
from sympy import Symbol, Limit, Derivative, solve, sympify, S, simplify, lambdify, pprint, init_printing, symbols
from fractions import Fraction

init_printing( order = 'rev-lex', use_unicode = True )

# 4.1.1

# Suppose a particle’s position is given by f (t) = t 4, 
# where t is measured in seconds and f (t) is given in centimeters. What is the velocity of the particle when t = 3?

Ft = t**4
t = Symbol( 't' )
Dt = Derivative( Ft, t ).doit()
Dt.subs( { t: 3 } )

# 4.1.2

# Suppose f(x) = x^-3. What is f'(x) ?

Fx = x**-3
x = Symbol( 'x' )
Derivative( Fx, x ).doit()

# 4.1.3

# Suppose f(x) = x^0. What is f'(x) ?

Fx = x**0.1
x = Symbol( 'x' )
Derivative( Fx, x ).doit()

# 4.1.6

# Suppose a particle's position is given by f(t) = t^4,
# where t is measurd in seconds and f(t) is given in meters.
# At what time is the velocity of the particle equal to 0 ?

Ft = t**4
t = Symbol( 't' )
Dt = Derivative( Ft, t ).doit()
sln = Dt.subs( { t: 1/2 } )

# 4.1.8

# Find the derivitve: -pi/3 ( sqrt(3) )

Fq = -1 * pi/3 * ( ( q ** 3 ) ** 1/2 )
q = Symbol( 'q' )
Derivative( Fq, q ).doit()

# 4.1.9

# Suppose f(x) = x^9. What is f'(x) ?

Fx = x**9
x = Symbol( 'x' )
Derivative( Fx, x ).doit()
