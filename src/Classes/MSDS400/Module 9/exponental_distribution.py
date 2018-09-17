from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )
# It is found that the time​ (in minutes) required by a predator to find a prey is a random variable that is exponentially distributed with

mu = 27

t = symbols( 't' )
a = 1/mu
pdf = a * exp( -a*t )

# According to this​ distribution, what is the longest time within which the predator will be 85​% certain of finding a​ prey?

pct = .85
x = symbols( 'x' )

prob = solve( Integral( pdf, ( t, 0, x ) ).doit() - pct, x )[ 0 ]
round( prob, 1 )

#  probability that the predator will have to spend more than 1 hour looking for a​ prey

prob = integrate( pdf, ( t, 60, oo ) ).doit()
round( prob, 4 )