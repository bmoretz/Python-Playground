# The date of the first sighting of robins has been occurring earlier each spring over the past 25 years at a certain laboratory. 
# Scientists from this laboratory have developed two linear​ equations, shown​ below, that estimate the date of the first sighting of​ robins, 
# where x is the year and y is the estimated number of days into the year when a robin can be expected. 

# Complete parts a and b. ​(Hint: 2000 was a leap​ year.)

# y = 771 - 0.353x
# y = 1663 - 0.796 x

import datetime
from sympy import symbols, solve

x, y = symbols( 'x, y' )

expr1 = 771 - 0.353*x - y
expr2 = 1663 - 0.796*x - y
year = 2000

if __name__== '__main__':

	offset1 = solve( expr1.subs( { x: year } ).evalf(), y )[ 0 ]
	offset2 = solve( expr2.subs( { x: year } ).evalf(), y )[ 0 ]

	print( offset1 )
	print( offset2 )

	d1 = datetime.datetime( 1999, 12, 31 ) + datetime.timedelta( days = int( offset1 ) )
	d2 = datetime.datetime( 1999, 12, 31 ) + datetime.timedelta( days = int( offset2 ) )

	print( d1 )
	print( d2 )

	soln = solve( ( expr1, expr2 ))

	round( soln[ x ], 0 )