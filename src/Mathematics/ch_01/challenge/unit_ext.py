'''
Unit converter: Miles to Kilometers
'''

def print_menu():
	print( '1. Kilometers to Miles' )
	print( '2. Miles to Kilometers' )
	print( '3. Fahrenheit to Celsius' )
	print( '4. Celsius to Fahrenheit' )

def km_miles():

	km = float( input( 'Enter distance in kilometers: ' ) )
	miles = km / 1.609

	print( 'Distance in kilometers: {0}'.format( km ) )

def miles_km():
	miles = float( input( 'Enter distance in miles: ' ) )
	km = miles * 1.609

	print( 'Distance in kilometers: {0}'.format( km ) )

def fahr_cels():
	f = float( input( 'Enter temp in Celsius: ' ) )
	c = ( f - 32 ) * ( 5 / 9 )

	print( 'Temp in Celsius: {0}'.format( c ) )

def cels_fahr():
	c = float( input( 'Enter temp in Fahrenheit: ' ) )
	f = c * ( 9 / 5 ) + 32

	print( 'Temp in Fahernheit: {0}'.format( f ) )

if __name__ == '__main__':
	print_menu()

	choice = input( 'Which conversion would you like to do?: ' )

	if( choice == '1' ):
		km_miles()

	if( choice == '2' ):
		miles_km()

	if( choice == '3' ):
		fahr_cels()

	if( choice == '4' ):
		cels_fahr()