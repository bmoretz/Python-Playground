'''
Sum a Series
'''

from sympy import symbols, summation, pprint, init_printing, sympify
from sympy.core import SympifyError

def sum_series( nterm, terms ):

	init_printing( order = 'rev-lex' )

	x, n = symbols( 'x, n' )

	s = summation( nterm, ( n, 1, terms ) )
	
	pprint( s )

if __name__ == '__main__':
	try:
		nterm = input( 'Enter the nth term: ' )
		terms = input( 'Enter the number of terms: ' )
	except SympifyError:
		print( 'Invalid Input' )
	else:
		sum_series( sympify( nterm ), terms )