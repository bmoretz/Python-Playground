from sympy import ( symbols, solve, diff, integrate, pprint )

# determine the value of k that makes f left parenthesis x right parenthesis a probability density function on

x, k = symbols( 'x, k' )
F = k*x**2

a, b = 0, 2

area = integrate( F, ( x, a, b ) )
val = solve( area - 1, k )

pprint( val[ 0 ] )