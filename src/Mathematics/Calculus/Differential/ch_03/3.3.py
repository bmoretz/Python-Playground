from math import sqrt, exp, log, sin
from sympy import Symbol, Limit, Derivative, solve, sympify, S, simplify, lambdify, pprint, init_printing, symbols
from fractions import Fraction

init_printing( order = 'rev-lex', use_unicode = True )

# 3.3.1

# Suppose f(x) = sqrt( x + 2 ).
# What is the slope of the line tangent to f when x = 3?

Fx = math.sqrt( x + 2 )
x = Symbol( 'x' )
d = Derivative( Fx, x ).doit()
Fd = d - 3
sln = solve( Fd, x )[ 0 ]

# 3.3.2

# Suppose a particle's position is given by f(t) = 3 * sqrt( t^2 + 5 )
# where t is measured in seconds and f(t) is given in centimeters.
# At what time is the velocity of the particle equal to 2?

Ft = 3 * ( t ** 2 + 5 ) ** .5
t = Symbol( 't' )
Dt = Derivative( Ft, t ).doit()
sln = solve( Dt - 2, t )[ 0 ]

# 3.3.3

# Find the derivative of f(x) = 1/4x

Fx = 1 / ( 4*x )
x = Symbol( 'x' )
dx = Derivative( Fx, x ).doit()
pprint( dx )

# 3.3.4

# Suppose a particle's position is given by f(t) = sqrt( 2t + 5 ),
# where t is given in centimeters. What is the velocity of the 
# particle when t = 2?

Ft = ( 2*t + 5 ) ** .5
t = Symbol( 't' )
Dt = Derivative( Ft, t ).doit()
sln = solve( Dt - 2 )[ 0 ]
pprint( float.as_integer_ratio( sln ) )

# 3.3.5

# Suppose a particle's position is given by
# f(t) = sqrt( t + 3 ), wehre t is measured in seconds, and f(t) is given
# in centimeters. What is the velocity of the particle when t = 1?

Ft = ( t + 3 ) ** .5
t = Symbol( 't', positive = True )
Dt = Derivative( Ft, t ).doit()
Dt = Dt - 1
sln = solve( Dt, t )
pprint( sln )

# 3.3.6

# Suppose f(x) = sqrt( x^2 + 5 ).
# Find the equation of the line tangent to f(x) at ( -2, 3 ).

x = Symbol( 'x', positive = True )
Fx = ( x** 2 + 5 ) ** .5

Fx

d = Derivative( Fx, x )
d

Dx = d.doit()
Dx

m = solve( d - 2, x )
m

x,y,m = symbols( 'x, y, m' )
line = m * ( x + 2 ) - y + 3
