'''
Product of two expressions
'''

from sympy import expand, sympify
from sympy.core.sympify import SympifyError

def product( expr1, expr2 ):
	prod = expand( expr1 * expr2 )
	print( prod )

if __name__ == '__main__':
	expr1 = input( 'Enter the first expression: ' )
	expr2 = input( 'Enter the second expression: ' )

try:
	expr1 = sympify( expr1 )
	expr2 = sympify( expr2 )
except:
	print( 'Invalid Input' )
else:
	product( expr1, expr2 )
