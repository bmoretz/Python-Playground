from sympy import *

# The projected population of a certain ethnic​ group(in millions) can be approximated by
t = symbols( 't' )
r = 1.012
P = 36.15 * ( r**t )
dP = diff( P, t )
years = 10

# The population in 2010 is
population = P.subs( { t: years } )
# (Round to three decimal places as​ needed.)
round( population, 3 )

# The instantaneous rate of change in the population when t=10
rate_of_change = dP.subs( { t: years } )
# (Round to three decimal places as​ needed.)
round( rate_of_change, 3 )