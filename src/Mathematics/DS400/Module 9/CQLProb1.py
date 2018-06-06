from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )

x = symbols( 'x' )
F = 0.003*x**2

def line( x0, y0, m ):
	x, y = symbols( 'x, y' )
	eq = m * ( x - x0 ) + y0 - y
	
	sln = solve( eq, y )

	return sln[0]

# [0,4] for F
a1 = integrate( F, ( x, 0, 4 ) )

# Find G
x1, y1 = 4, 0.048
x2, y2 = 43, 0
m = ( y2 - y1 ) / ( x2 - x1 )

G = line( x1, y1, m )

# Area [4, 43]
a2 = integrate( G, ( x, 4, 43 ) )

a1 + a2

#  Find the value of the probability ​P( x <3 ​).
integrate( F, ( x, 0, 3 ) )

# Find the value of the probability P( 1 < x < 23.8 )

prob_f = integrate( F, ( x, 1, 4 ) )
prob_g = integrate( G, ( x, 4, 23.8 ) )

round( prob_f + prob_g, 5 )