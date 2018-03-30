
from sympy import Symbol, solve, Derivative

x = Symbol( 'x' )
f = x**5 - 30*x**3 + 50*x

d1 = Derivative( f, x ).doit()

critical_points = solve( d1 )

critical_points

A = critical_points[ 2 ]
B = critical_points[ 0 ]
C = critical_points[ 1 ]
D = critical_points[ 3 ]

d2 = Derivative( f, x, 2 ).doit()

d2.subs( { x: B } ).evalf()
d2.subs( { x: C } ).evalf()
d2.subs( { x: A } ).evalf()
d2.subs( { x: D } ).evalf()

x_min = -5
x_max = 5

f.subs( { x: C } ).evalf()
f.subs( { x: A } ).evalf()

f.subs( { x: x_min } ).evalf()
f.subs( { x: x_max } ).evalf()
