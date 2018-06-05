from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )

# Over​ time, the number of original basic words in a language tends to decrease as words become obsolete or are replaced with new words. 
# For a certain​ language, the proportion of words that remain after t millennia is a random variable that is exponentially distributed with


t = symbols( 't' )
a = 0.298
mu = 1/a
pdf = a * exp( -a*t )

# What is the life​ expectancy?

round( mu, 2 )

a, b = 3, oo
prob = integrate( pdf, ( t, a, b ) ).doit()
round( prob, 4 )














































































