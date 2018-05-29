from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )

# The length​ (in centimeters) of a petal on a certain flower is a random variable with probability density function defined by ​

x = symbols( 'x' )
F = 1 / ( 4 * sqrt( x ) )

# for x in ​[4​,16​].

a, b = 4, 16

def mean( f, var, a, b ):
	return integrate( var * f, ( var, a, b ) )

def variance( f, var, a, b, mu ):
	return integrate( ( ( var **2 ) * f ), ( var, a, b ) ) - mu**2

def std_dev( var ):
	return sqrt( var )

# The expected petal length is
mu = round( mean( F, x, a, b ), 3 )

# The standard deviation is
var = round( variance( F, x, a, b, mu ), 3 )
stdev = round( sqrt( var ), 3 )

# The probability that a petal selected at random has a length less than 2 standard deviations below the mean is
prob_within_1sd = integrate( F, ( x, 4,  mu - stdev * 2 ) )
round( prob_within_1sd, 2 ) # Not in bounds

# mean
m = symbols( 'm' )
mf = Integral( F, ( x, a, m ) ).doit()
median = solve( mf - .5 , m )[ 0 ]