from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )

# The annual rainfall in a remote country varies from 0 to 7 inches and is a random variable with probability density function defined by
x = symbols( 'x' )
F = ( 7.5 - x ) / 28

# [0,7]
a, b = 0, 7

def mean( f, var, a, b ):
	return integrate( var * f, ( var, a, b ) )

def variance( f, var, a, b, mu ):
	return integrate( ( ( var **2 ) * f ), ( var, a, b ) ) - mu**2

# The expected petal length is
mu = mean( F, x, a, b )

# The standard deviation is
var = variance( F, x, a, b, mu )
stdev = round( sqrt( var ), 2 )

# The probability of a year with rainfall less than 1 standard deviation below the mean is approximately:
prob_within_1sd = integrate( F, ( x, 0, round( mu, 2 ) - round( stdev, 2 ) ) )
round( prob_within_1sd, 2 )
