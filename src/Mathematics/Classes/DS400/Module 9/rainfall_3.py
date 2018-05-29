from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )
# Researchers have shown that the number of successive dry days that occur after a rainstorm for a particular region is a random variable that is distributed exponentially with a mean of 9 days

mu = 9

t = symbols( 't' )
a = 1/mu
pdf = a * exp( -a*t )

# What is the probability that 11 or more successive dry days occur after a​ rainstorm?

prob = integrate( pdf, ( t, 11, oo ) ).doit()
round( prob, 4 )

# What is the probability that fewer than 4 dry days occur after a​ rainstorm?

prob = integrate( pdf, ( t, 0, 2 ) ).doit()
round( prob, 4 )