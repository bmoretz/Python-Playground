import math
import numpy as np

def correlation( x, y ):
	if len( x ) != len( y ):
		print( 'arrays must have same dimension' )
	else:
		n = len( x )

		xy = x*y
		xsq = x ** 2
		ysq = y ** 2

		m1 = n * sum( xy ) - sum( x ) * sum( y )
		m2 = n * sum( xsq ) - sum( x ) ** 2

		m = m1/m2

		b = ( sum( y ) - m * sum( x ) ) / n

		return m, b

if __name__ == '__main__':

	x = np.array( [ 20.00, 30.00, 40.00, 50.00, 60.00, 70.00, 80.00, 90.00, 100.00, 110.00 ] )
	y = np.array( [ 71.20, 80.50, 73.40, 60.30, 52.10, 56.20, 46.50, 36.90, 34.00, 39.10 ] )

	correlation( x, y )
