from math import sqrt, exp, log, sin, pi
from sympy import Symbol, Limit, Derivative, solve, sympify, S, simplify, lambdify, pprint, init_printing, symbols
from fractions import Fraction

init_printing( order = 'rev-lex', use_unicode = True )

# 4.2.1

# Suppose f (x) = (4x 3 + 3) (1 − x 2 ). 
# What is the equation of the line tangent to f at the point (1, 0)?

x0 = 1
y0 = 0

Fx = ( 4*x**3 + 3 ) * ( 1 - x ** 2 )
x = Symbol( 'x' )
Dx = Derivative( Fx, x ).doit()

m = Dx.subs( { x: x0 } )
x1 = Fx.subs( { x: x0 } )

# 4.2.2

# Suppose f (x) = (x 2 − 2x) (3x + 2).
# What is the equation of the line normal to f
# (i.e., the line perpendicular to the tangent line)
# at the point (1, −5)?

x0 = 1
y0 = -5

Fx = ( x ** 2 - 2*x ) * ( 3*x + 2 )
x = Symbol( 'x' )
Dx = Derivative( Fx, x ).doit()

m = Dx.subs( { x: x0 } )
m1 = -1/m

# Line
y = m1 * ( x - x0 ) + y0

# 4.2.3

# Find the derivative: f(x) = ( x -2 ) / x^2

Fx = ( x - 2 ) / x ** 2
x = Symbol( 'x' )
Derivative( Fx, x ).doit()

# 4.2.4

# Find the derivative: f(x) = x^2 + 1 / x + 1

Fx = ( x ** 2 + 1 ) / ( x + 1 )
x = Symbol( 'x' )
Derivative( Fx, x ).doit()

# 4.2.5

# Find the derivative:
# v(x) =  ( x + 2 ) ^ 1/2 / ( x - 3 ) ^ 1/3

Vx = ( ( x + 2 ) ** 1/2 ) / ( ( x - 3 ) ** 1/3 )
x = Symbol( 'x' )
Derivative( Vx, x ).doit()

# 4.2.6

# Find the derivative:
# f(x) = ( x + 2 ) ^ 4/3 / 2x
Fx = ( x + 2 ) ** 4/3 / 2*x
x = Symbol( 'x' )
Derivative( Fx, x ).doit()

# 4.2.7

# Find the derivative:
# h(x) = ( 2*x**4 + 3*x + 7 ) * ( x**5 - 3*x**2 )
Fx = ( 2*x**4 + 3*x + 7 ) * ( x**5 - 3*x**2 )
x = Symbol( 'x' )
Derivative( Fx, x ).doit()

# 4.2.8

# Suppose f (x) = (3x − x 2 ) (2x − x 2 ). 
# Find the equation of the line tangent to f at the point (1, 2).

x0 = 1
y0 = 2

Fx = ( 3 * x - x**2 ) * ( 2 * x - x**2 )
x = Symbol( 'x' )
Dx = Derivative( Fx, x ).doit()

m = Dx.subs( { x: x0 } )

# Line
y = m1 * ( x - x0 ) + y0

# 4.2.9

# Find the derivative:
# f(x) = ( t + 3 ) ** 1/2 / ( t - 3 ) ** 3/2
Fx = ( t + 3 ) ** 1/2 / ( t - 3 ) ** 3/2
x = Symbol( 'x' )
Derivative( Fx, x ).doit()
