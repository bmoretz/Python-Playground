from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )

# The amount of insurance​ (in thousands of​ dollars) sold in a day by a particular agent is uniformly distributed over the interval ​[10, 70​].

a, b = 10, 70
# What amount of insurance does the agent sell on an average​ day? (Thousands)
mean = .5*( b + a ) * 1000

x = symbols( 'x' )
#Find the probability that the agent sells more than ​$50​,000 of insurance on a particular day.
pdf = 1 / ( b - a ) * x

# The probability that one of these​ insects, randomly​ selected, lives longer than 27 days is
prob = integrate( pdf * 1/x, ( x, 50, b ) )
round( prob, 4 )