from sympy import Symbol, Derivative

t = Symbol( 't' )
St = 5*t**2 + 2*t + 8

d = Derivative( St, t )
d.doit()

d.doit().subs( { t : 1 } )


x = Symbol( 'x' )
f = ( x ** 3 + x ** 2 + x ) * ( x**2 + x )
Derivative( f, x ).doit()