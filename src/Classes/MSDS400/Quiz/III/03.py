from sympy import *

# Based on a study of population projections for 2000 to​ 2050, 
# the projected population of a group of people​ (in millions) can be modeled by the following exponential​ function, 
# where t=0 corresponds to 2000 and 0 <= t <= 50.

t = symbols( 't', positive = True )
r = 1.078
A = 11.27*r**t
years = 14

r = 1.078
A = 11.27*r**t
years = 14

a = A.subs( { t: years } )
b = A.subs( { t: 0 } )

avg_chg = round( ( a - b ) / years, 3 )
round( avg_chg * 1000000 ) # Estimate the average rate of change in the population from 2000 to 2014.

dA = Derivative( A, t ).doit()
instanious_rate_of_change = dA.subs( { t: years } )
round( instanious_rate_of_change, 3 ) * 1000000 # Estimate the instantaneous rate of change in the population in 2014.