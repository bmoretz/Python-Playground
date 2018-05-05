# The sales of a new​ high-tech item​ (in thousands) are given by:

# S(t) = 108 - 90e^-0.4t

# where t represents time in years. Find the rate of change of sales at each time.

from sympy import *
import math
import mpmath as mp

init_printing()

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

t = symbols( 't' )
S = 110 - ( 90 * exp( -0.4*t ) )
dS = diff( S, t )

disp_fun( S )
disp_fun( dS )

# ​a.) After 1 year.​ (Round to three decimal places as​ needed.)
round( dS.subs( { t: 1 } ), 3 )

# b.) After 5 years.​
round( dS.subs( { t: 5 } ), 3 )

# c.) What is happening to the rate of change of sales as time goes​ on?

print( 'It always decreases' )

# d.) Does the rate of change of sales ever equal​ zero?
print( 'No' )
