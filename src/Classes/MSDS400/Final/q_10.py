from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )
# The time between goals​ (in minutes) for a professional soccer team during a recent season can be approximated by an exponential distribution with

mu = 90

t = symbols( 't' )
a = 1/mu
pdf = a * exp( -a*t )

# What is the probability that the time for a goal is no more than 69 ​minutes?
prob = integrate( pdf, ( t, 0, 69 ) ).doit()
round( prob, 4 )

# What is the probability that the time for a goal is 494 minutes or​ more?
prob = integrate( pdf, ( t, 494, oo ) ).doit()
round( prob, 4 )