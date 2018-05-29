from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )

# The clotting time of blood​ (in seconds) is a random variable with probability density function defined by

x = symbols( 'x' )
F = 1 / ( ln( 27 ) * x )

# for x in ​[1, 27​].

a, b = 1, 27

def expected_value( f, var, a, b ):
	return integrate( var * f, ( var, a, b ) )

def variance( f, var, a, b, mu ):
	return integrate( ( ( var **2 ) * f ), ( var, a, b ) ) - mu**2

def std_dev( var ):
	return sqrt( var )

def expected_value( f, var, a, b ):
	return integrate( var * f, ( var, a, b ) )

mu = round( expected_value( F, x, a, b ).evalf(), 2 )
mu

# Find the standard deviation of the distribution.
var = round( variance( F, x, a, b, mu ).evalf(), 2 )
var

stdev = round( std_dev( var ), 2 )
stdev

# ind the probability that the value of the random variable is within one standard deviation of the mean.
prob_within_1sd = integrate( F, ( x, mu - stdev, mu + stdev ) )
round( prob_within_1sd.evalf(), 2 )

# Find the median clotting time.
mean = exp( ( ln( 27 ) /2 ).evalf() )
round( mean, 2 )