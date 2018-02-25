
from sympy import sympify, init_printing
from sympy.core.sympify import SympifyError

init_printing( order = 'rev-lex' )

expr = input( 'Enter a mathematical expression: ' )

try:
	expr = sympify( expr )
	expr
except:
	print( 'Invalid Input' )

