from sympy import symbols, sympify, factor, pprint, init_printing, plot
from sympy.core import SympifyError

init_printing( order = 'rev-lex' )

def graph_system( expr1, expr2 ):

	y = symbols( 'y' )

	expr1_sln = solve( expr1, y ) 
	expr2_sln = solve( expr2, y )

	p = plot( expr1_sln[ 0 ], expr2_sln[ 0 ], legend = True, show = False )

	p[ 0 ].line_color = 'b'
	p[ 1 ].line_color = 'r'

	sln = solve( ( expr1, expr2 ), symbols( 'x, y' ) )

	pprint( sln )

	p.show()
	
if __name__== '__main__':

	try:
		expr1 = input( 'Enter an expression in terms of x and y: ' )
		expr2 = input( 'Enter an expression in terms of x and y: ' )
		
		expr1 = sympify( expr1 )
		expr2 = sympify( expr2 )
	except SympifyError:
		print( 'Invalid Input' )
	else:
		graph_system( expr1, expr2 )