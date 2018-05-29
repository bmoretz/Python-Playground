from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, pprint, oo )

# The life​ (in years) of a certain machine is a random variable with probability density function defined by

x = symbols( 'x' )
F = 1/84 * ( 5 + 1/sqrt( x ) )

# for x in ​[9​, 25​].

a, b = 9, 25

def expected_value( f, var, a, b ):
	return integrate( var * f, ( var, a, b ) )

def variance( f, var, a, b, mu ):
	return integrate( ( ( var **2 ) * f ), ( var, a, b ) ) - mu**2

mu = expected_value( F, x, a, b )

round( mu, 2 )

# Find the standard deviation of the distribution.
variance = variance( F, x, a, b, mu )
round( sqrt( variance ), 2 )

# Find the probability that a particular machine of this kind will last longer than the mean number of years.
prob_gt_mean = integrate( F, ( x, mu, b ) )
round( prob_gt_mean, 2 )