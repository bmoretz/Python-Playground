from sympy import solve, symbols, lambdify, diff, pprint, pretty, simplify, Derivative
import matplotlib.pyplot as plt
import numpy as np

# Based on a study of population projections for 2000 to​ 2050, 
# the projected population of a group of people​ (in millions) can be modeled by the following exponential​ function, 
# where t=0 corresponds to 2000 and 0 <= t <= 50.

def rate_of_change( f, a, b ):
	return ( f.subs( { t: b } ) - f.subs( { t: a } ) ) \
	/ ( b - a )

t = symbols( 't', positive = True )

r = 1.013
A = 38.25 * ( r ) ** t
years = 10

# se A to estimate the average rate of change in the population from 2000 to 2012.

a = round( A.subs( { t: years } ), 2 )
b = round( A.subs( { t: 0 } ), 2 )

chg = ( a - b ) / years

h  = 0.001

roc = rate_of_change( A, years + h, years )

( a * ( b * ( r**h ) - 1 ) ) / h

diff( A, t ).subs( { t: 10 } )