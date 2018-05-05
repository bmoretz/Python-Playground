from sympy import symbols, solve, pprint, Derivative
import math

dec_places = 4
value = .6

x = symbols( 'x' )

fX = ( x ** 2 ) / ( 2 * ( 1 - x ) )
pprint( fX )

dX = Derivative( fX, x ).doit()
pprint( dX )

res = dX.subs( { x: value } )

# ​(Simplify your answer. Type an integer or decimal rounded to four decimal places as​ needed.) 
print( 'The rate of change for {0} at {1} is {2}'.format( fX, value, round( res, dec_places ) ) )