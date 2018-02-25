from sympy import symbols, sympify, factor, pprint, init_printing
from sympy.core import SympifyError

init_printing( order = 'rev-lex' )

def find_factors( expr ):
	factors = factor( expr )
	pprint( factors )

if __name__== '__main__':

	try:
		expr = input( 'Enter an expression to Factor: ' )
		expr = sympify( expr )
	except SympifyError:
		print( 'Invalid Input' )
	else:
		find_factors( expr )
