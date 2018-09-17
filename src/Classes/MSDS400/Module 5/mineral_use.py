#To test an​ individual's use of a certain​ mineral, a researcher injects small amount of a radioactive form of that mineral into the​ person's bloodstream.  
#The mineral remaining in the bloodstream is measured each day for several days.  
#Suppose the amount of the mineral remaining in the bloodstream​ (in milligrams per cubic​ centimeter) t days after the initial injection is approximated by 

# C(t) = 1/2 ( 4t + 4) ^ -1/2

# Find the rate of change of the mineral level with respect to time for 7.5 days.

from sympy import symbols, solve, pprint, Derivative, init_printing, pretty
import math

init_printing()

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

t = symbols( 't' )
C = .5*( 4*t + 4 ) ** -(.5)

disp_fun( C )

dC = Derivative( C, t ).doit()

# The rate of change of the mineral level with respect to time for 7.5 days is approximately 
# nothing milligrams per cubic centimeter per day.
​# (Round to two decimal places as​ needed.)

round( dC.subs( { t: 7.5 } ), 2 )