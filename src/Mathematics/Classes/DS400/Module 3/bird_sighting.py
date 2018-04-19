# The date of the first sighting of robins has been occurring earlier each spring over the past 25 years at a certain laboratory. 	
# Scientists from this laboratory have developed two linear​ equations, shown​ below, that estimate the date of the first sighting of​ robins, where x is the year and y is the estimated number of days into the year when a robin can be expected. 	
#Complete parts a and b. ​(Hint: 2000 was a leap​ year.)	
	
# y = 819 - 0.371x
# y = 1632 - 0.779x

import datetime
from sympy import symbols, solve

x, y = symbols( 'x,y' )

expr1 = 819 - 0.371*x - y
expr2 = 1632 - 0.779*x - y

year = 2000
expr1.subs( { x: year } ).evalf() 
expr2.subs( { x: year } ).evalf() 

datetime.datetime( 2000, 1, 1 ) + datetime.timedelta( days = 77 )
datetime.datetime( 2000, 1, 1 ) + datetime.timedelta( days = 74 )

soln = solve( ( expr1, expr2 ), dict = True )

soln