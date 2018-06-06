'''
Multiplication table printer
'''

def multi_table_ext( a, e ) :
	for i in range( 1, e + 1 ) :
		print( '{0} x {1} = {2}'.format( a, i, a * i ) )

if __name__ == '__main__':
	try:
		a = float( input( 'Enter a number: ' ) )
		e = int( input( 'Enter a range: ' ) )
		multi_table_ext( a, e )
	except ValueError:
		print( "Invalid Number." )