from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )

# The life span of a certain insect​ (in days) is uniformly distributed over the interval [18, 32].

a, b = 18, 32
mu = .5 * ( b + a )

x = symbols( 'x' )
pdf = 1 / ( b - a ) * x

# The expected life of this insect is 
mu

# The probability that one of these​ insects, randomly​ selected, lives longer than 28 days is
prob = integrate( pdf * 1/x, ( x, 28, b ) )
round( prob, 4 )