import math
from sympy import sin, solve, symbols, Symbol, Limit

# Solve for T
u, t, g, theta = symbols( 'u, t, g, theta' )
solve( u * sin( theta ) -g*t, t )

x = Symbol( 'x', positive = True )
if( x + 5 ) > 0:
	print( '+' )
else:
	print( '-' )

# Indeterminant Form

Limit( sin(x) / x, x, 0 ).doit()