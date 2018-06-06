'''
Gravitational Motion
'''

from matplotlib import pyplot as plt
import math

def draw_graph( x, y ) :
	plt.plot( x, y, marker = 'o' )
	plt.xlabel( 'Distance in meters' )
	plt.ylabel( 'Gravitational force in newtons' )
	plt.title( 'Gravitational force and distance' )
	
def frange( start, end, increment ):

	numbers = []

	while start < end:
		numbers.append( start )
		start = start + increment

	return numbers

def draw_trajectory( u, theta ):

	theta = math.radians( theta )
	g = 9.8

	# Flight Time
	t_flight = 2 * u * math.sin( theta ) / g

	# Time Intervals
	intervals = frange( 0, t_flight, 0.001 )
	
	# X & Y
	x = []
	y = []
	for t in intervals:
		x.append( u * math.cos( theta ) * t )
		y.append( u * math.sin( theta ) * t - 0.5 * g * t * t )

	draw_graph( x, y )

if __name__ == '__main__':
	try:
		u = float( input( 'Enter the inital velocity ( m/s): ' ) )
		theta = float( input( 'Enter the angle of projection (degrees) : ' ) )

	except ValueError:
		print( 'You entered an invalid input.' )
else:
	draw_trajectory( u, theta )
	plt.show()


u_list = [ 20, 40, 60 ]
theta = 45

for u in u_list:
	draw_trajectory( u, theta )

plt.legend( [ '20', '40', '60' ] )
plt.show()
