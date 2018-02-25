from sympy import Poly, symbols, sympify, pprint, solve_poly_inequality, solve_rational_inequalities, solve_univariate_inequality
from sympy.core import SympifyError

def isolve( expr ):
	
	x = symbols( 'x' )
	ineq_obj = sympify( expr > 0 )
	lhs = ineq_obj.lhs
	rel = ineq_obj.rel_op

	sln = 0

	if expr.is_polynomial():

		p = Poly( lhs, x )
	
		sln = solve_poly_inequality( p, rel )

		return sln

	elif expr.is_rational_function():
		
		numer, denom = lhs.as_numer_denom()

		p1 = Poly( numer )
		p2 = Poly( denom )

		sln = solve_rational_inequalities( [ [ ( ( p1, p2 ), rel ) ] ] )

	else:
		sln = solve_univariate_inequality( ineq_obj, x, relational = False )

	return sln

# expr = '-x**2 + 4'
# expr = '( x - 1 ) / ( x + 2 )'
# expr = 'sin( x ) - 0.6'

try:
	expr = input( 'Enter an expression to solve for: ' )
	expr = sympify( expr )

except SympifyError:
	print( 'Invalid Input' )
else:
	pprint( isolve( expr ) )