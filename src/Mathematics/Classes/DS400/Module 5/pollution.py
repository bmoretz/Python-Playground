# When there is a thermal inversion layer over a​ city, pollutants cannot rise vertically but are trapped below the layer and must disperse horizontally. 
# Assume that a factory smokestack begins emitting a pollutant at 8 a.m. 
# 
# Assume that the pollutant disperses​ horizontally, forming a circle. 
# 
# If t represents the time​ (in hours) since the factory began emitting pollutants​ (t = 0 represents 8​ a.m.), assume that the radius of the circle of pollution is r(t) = 4t miles. 
# 
# Let Upper A( r ) = pi r^2, the area of a circle of radius r. Complete parts​ (a) and​ (b).

from sympy import symbols, solve, pprint, Derivative, init_printing, pretty
import math

init_printing()

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

t, pi = symbols( 't, pi' )

r = 4*t
A = ( r ** 2 ) * pi

disp_fun( A )

dA = Derivative( A, t ).doit()

# dA/dT
disp_fun( dA )

# dA/dT @ t = 6
disp_fun( dA.subs( { t: 6 } ) )