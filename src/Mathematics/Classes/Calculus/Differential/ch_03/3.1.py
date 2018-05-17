import math
from sympy import Symbol, Limit, Derivative, sympify, S, simplify, pprint, init_printing

init_printing( order = 'rev-lex', use_unicode = True )


# 3.1.1

# h(t) = e^t + 2t^2
# simplify the expression:
# ( h( 5 + Dt ) - h( 5 ) ) / Dt

Ht = math.e**t + 2*t**2
t = Symbol( 't' )
delta_t = Symbol( 'delta_t' )

Ht1 = Ht.subs( { t: 5 } )
Ht1_delta = Ht.subs( { t: 5 + delta_t } )

f = ( Ht1_delta - Ht1 ) / delta_t

simplify( f )

Limit( f, delta_t, 0 ).doit()

# 3.1.2

# Suppose f(x) = -2x^2.
# What is the instantaneous rate of change of f(x) when x = 4?

Fx = -2*x**2
x = Symbol( 'x' )
d = Derivative( Fx, x ).doit()
d.subs( { x: 4 } )

# 3.1.3

# A particular bird's flight position in feet is given by the equation P(t) = 12t^2/7 +t, where
# t is the number of seconds that elapse.
# What is the bird's instantaneous velocity when t = a?
Pt = 12*t**2 / 7 + t
t = Symbol( 't' )
a = Symbol( 'a ' )
d = Derivative( Pt, t ).doit()
d.subs( { t: a } )

# 3.1.5

# A biker rides along a horizontal straight line with its location given by the fraction,
# s(t) = (1/10)t^2, where t is measured in minutes and s is in miles.
# To estimate the instantaneous velocity at time t = 2 minutes, 
# compute the average rate of change from t = 1.9 to t = 2.0 minutes.

St = 1/10*t**2
t = Symbol( 't' )

t1 = 2.0
St1 = St.subs( { t: t1 } )

t2 = 1.9
St2 = St.subs( { t: t2 } )

( St1 - St2 ) / ( t1 - t2 )

# 3.1.6

# Suppose f(x) = x^2 - 3. 
# What is the slope of the line tangent to f(x), at x = 3?

Fx = x**2 - 3
x = Symbol( 'x' )
d = Derivative( Fx, x ).doit()
d.subs( { x: 3 } )

# 3.1.7

# Given taht f(t) = 2t^2 - 4t and f'(x) = 4t - 4,
# find the instantaneous rate of change at t = 3.

FPx = 4*t - 4
t = Symbol( 't' )
FPx.subs( { t: 3 } )

# 3.1.8

# A bowling ball's position as it rolls down the lane is described by the position function,
# s(t) = 5t - 1/8t**2, where t is in seconds and s(t) is in feet. What is the bowling ball's
# instantanous velocity at t = 4?

St = 5*t - (1/8)*t**2
t = Symbol( 't' )
d = Derivative( St, t ).doit()
d.subs( { t: 4 } )

# 3.1.10

# Consider the curve f(x) = 4x^2, 0 <= x <= 3.
# What is the greatest possible slope of a secant line across
# interval of width .1 ?

Fx = 4*x**2
x = Symbol( 'x' )

interval = .1
p_max = 3

( Fx.subs( { x: p_max } ) - Fx.subs( { x: p_max - interval } ) ) / interval
