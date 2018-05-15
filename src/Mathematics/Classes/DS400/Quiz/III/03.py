from sympy import *

# Based on a study of population projections for 2000 to​ 2050, 
# the projected population of a group of people​ (in millions) can be modeled by the following exponential​ function, 
# where t=0 corresponds to 2000 and 0 <= t <= 50.

def avg_rate_of_change( f, a, b ):
	return ( f.subs( { t: b } ) - f.subs( { t: a } ) ) \
	/ ( b - a )

t = symbols( 't', positive = True )

r = 1.065
A = 11.11*r**t
years = 12

# use A to estimate the average rate of change in the population from 2000 to 2012.

a = round( A.subs( { t: years } ), 0 )
b = round( A.subs( { t: 0 } ), 0 )

chg = ( a - b ) / years
round( chg, 3 )

dA = Derivative( A, t ).doit()
instanious_rate_of_change = dA.subs( { t: years } )
round( instanious_rate_of_change, 3 )