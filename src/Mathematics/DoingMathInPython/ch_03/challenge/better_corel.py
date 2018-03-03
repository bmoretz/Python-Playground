import math

def find_corr_x_y( x, y ):
	
	n = len( x )
	z = len( y )

	if n != z:
		raise ValueError( 'Correlation cannot be evaluated with different length sets ( x:len[{0}] / y:len[{1}] )'.format( n, z ) )

	prod = []

	for xi, yi in zip( x, y ):
		prod.append( xi * yi )

	sum_prod_x_y = sum( prod )

	sum_x = sum( x )
	sum_y = sum( y )

	squared_sum_x = sum_x ** 2
	squared_sum_y = sum_y ** 2

	x_square = []
	for xi in x:
		x_square.append( xi ** 2 )
	x_square_sum = sum( x_square )

	y_square = []
	for yi in y:
		y_square.append( yi ** 2 )
	y_square_sum = sum( y_square )

	numerator = n * sum_prod_x_y - sum_x * sum_y

	denominator_term1 = n * x_square_sum - squared_sum_x

	denominator_term2 = n * y_square_sum - squared_sum_y

	denominator = ( denominator_term1 * denominator_term2 ) ** .5

	correlation = numerator / denominator

	return correlation

if __name__ == '__main__':

	x = [ 90, 92, 95, 96, 87, 87, 90 ,95, 98 ]
	y = [ 85, 87, 86, 97, 96, 88, 89, 98, 98, 87 ]

	try:
		correl = find_corr_x_y( x, y )
		print( correl )
	except ValueError as e:
		print( e )