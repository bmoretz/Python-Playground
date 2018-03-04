'''
Draw Hénon’s function

'''

import random
import matplotlib.pyplot as plt

def transform( p ):

	x = p[ 0 ]
	y = p[ 1 ]

	x1 = ( y + 1 ) - ( 1.4*x**2 )
	y1 = 0.3*x

	return x1, y1

def draw_henons( n ):
	x = [ 0 ]
	y = [ 0 ]

	x1, y1 = 1, 1

	for i in range( n ):
		x1, y1 = transform( ( x1, y1 ) )
		x.append( x1 )
		y.append( y1 )
	return x, y

if __name__ == '__main__':

	try:
		n = int( input( 'Enter the number of points: ' ) )
	except ValueError:
		print( 'Invalid Input' )
	else:
		x, y = draw_henons( n )

		plt.plot( x, y, 'o' )
		plt.title( 'Hénon’s function with {0} points'.format( n ) )
		plt.show()