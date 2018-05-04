
'''
Units of Measurment
'''

''' Inches ->> Meters '''

( 25.5 * 2.54 ) / 100

''' Mile ->> KM '''
650 * 1.609

''' Fahrenheit ->> Celsius '''

F = 98.6

( F - 32 ) * ( 5 / 9 )

def to_celsius( f ):
	print( ( f - 32 ) * ( 5 / 9 ) )

def to_fahrenheit( c ) :
	print( c * ( 9 / 5 ) + 32 )