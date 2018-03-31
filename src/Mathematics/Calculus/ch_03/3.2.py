import math
from sympy import Symbol, Limit, Derivative, solve, sympify, S, simplify, lambdify, pprint, init_printing

init_printing( order = 'rev-lex', use_unicode = True )

# 3.2.1

# A particle moves along a straight line with its position give by the function:
# p = f(t) = t^2 -2t +4,
# where p is given in meters and t in seconds.
# When does the velocity equal zero?

Pt = t**2 - t*2 + 4
t = Symbol( 't' )
d = Derivative( Pt, t ).doit()
sln = solve( d, t, dict = True )
pprint( sln[ 0 ] )

# 3.2.1

# Suppose f(X) = x^2 - 3x
# What is the equation of the line tangent to the curve at the point ( 2, -2 ) ?

# 3.2.4

# A particle moves along a straight line with its position given by the function
# p = f(t) = 3t^2 - 2t + 4, where p is given in meters and t in seconds.
# For what value of t does the velocity of the particle equal 10 MPS?

Pt = 3*t**2 - t*2 + 4
t = Symbol( 't' )
d = Derivative( Pt, t ).doit()

# Solve for t = 10
Ds = d - 10
sln = solve( Ds, t, dict = True )
pprint( sln[ 0 ] )

# 3.2.5

# At what point is the slope of the line tangent to curve 
# y = x^2 - 2x + 1 equal to 2?

Fx = x**2 - 2*x + 1
x = Symbol( 'x' )
d = Derivative( Fx, x ).doit()

# solve for x = 2
Ds = d - 2
px = solve( Ds, x )[ 0 ]
py = Fx.subs( { x: px } )

pprint( '( {0}, {1} )'.format( px, py ) )

# 3.2.6

# A child kicks a soccer ball across a field. The distance between the soccer ball and
# the child in feet is given by the formula:
# p(t) = 25t - t^2, 0 <= t < 25, where t is measured in seconds.
# How fast is the soccer ball moving when t = 5 seconds?

Pt = 25*t - t**2
t = Symbol( 't', positive = True )
d = Derivative( Pt, t ).doit()
d.subs( { t: 5 } )

# 3.2.7

# The rate of production at ACME toys can be determined from the production formula P(t) = 1600t - 100t^2, 
# where P(t) is the number of units produced in a given time and t is the time in hours since the factory shift
# began. At what time does the rate of toy production stop?

Pt = 1600*t - 100*t**2
t = Symbol( 't' )
d = Derivative( Pt, t ).doit()
solve( d, t )[ 0 ]

# 3.2.8

# A student goes crabbing after math class. He drops the crab cage, and waits. Let f(t) denote the distance
# a crab is from the cage at any time. Assume f(t) = -2t^2 - 7t + 15, where t is measured in hours, and
# f(t) is in feet. How long does the student need to wait before the crab is in the cage?

Ft = -2*t**2 - 7*t + 15
t = Symbol( 't', positive = True )
solve( Ft, t )

# 3.2.10

# Consider the function f(x) = x^2 - x. Using the fact that f'(x) = 2x -1, find the point (x,y) on the
# graph of f(x) where the tangent line is a horizontal line.

Fx = x**2 - x
FPx = 2*x -1
x = Symbol( 'x', positive = True )

# Tangent line is horizontal where f'(x) = 0
px = solve( FPx, x )[ 0 ]
# y value = f( f'( 0 ) )
py = Fx.subs( { x: px } )

pprint( '( {0}, {1} )'.format( px, py ) )