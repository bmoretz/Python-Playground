from sympy import Limit, Symbol, sympify
from sympy.core.sympify import SympifyError

f = '1/x'

result = ( "is not", "is" )

def is_continious( f, v, p ):
	fx = sympify( f )
	s = Symbol( v )
	lf = Limit( fx, s, p ).doit()
	return lf == p

if __name__ == '__main__':

	try:
		f = input( 'Enter a function in one variable: ')
		v = input( 'Enter the variable: ' )
		p = float( input( 'Enter the point to check the continuity at: ' ) )
	except SympifyError:
		print( 'Error parsing the function' )
	else:
		continuity = is_continious( f, v, p ) 
		print( '{0} {1} continuous at {2}'.format( f, result[ continuity ], p ) )