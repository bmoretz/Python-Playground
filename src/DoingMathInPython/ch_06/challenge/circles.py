'''
Pack Circles into a Square
'''

from matplotlib import pyplot as plt

def draw_circle( x, y ):

	circle = plt.Circle( ( x, y ), radius = 0.5 )
	circle.set_fc( 'r' )
	return circle

def fill_square():

	ax = plt.axes( xlim = ( 0, 6 ), ylim = ( 0, 6 ) )
	square = plt.Polygon( [ ( 1, 1 ), ( 5, 1 ), ( 5, 5 ), ( 1, 5 ) ], closed = True )
	ax.add_patch( square )

	y = 1.5
	
	while y < 5:
		x = 1.5
		while x < 5:
			c = draw_circle( x, y )
			
			ax.add_patch( c )
			x += 1.0
		y += 1

if __name__ == '__main__':
	fill_square()
	plt.show()