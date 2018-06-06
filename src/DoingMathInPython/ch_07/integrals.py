from sympy import Integral, Symbol

x = Symbol( 'x' )
k = Symbol( 'k' )
Integral( k*x, x ).doit()

Integral( k*x, ( x, 0, 2 ) ).doit()

Integral( x, ( x, 2, 4 ) ).doit()

