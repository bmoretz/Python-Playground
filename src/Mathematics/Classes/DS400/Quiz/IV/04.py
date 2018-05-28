from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, pprint, Integral )

# The rate at which a substance grows is given by

x = symbols( 'x' )
R = 195*exp( 0.3 * x )

a, b = 0, 2.5
growth = integrate( R, ( x, a, b ) )
round( growth, 1 )