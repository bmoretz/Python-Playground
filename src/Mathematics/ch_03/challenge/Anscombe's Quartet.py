import collections
import csv
import math
import os

def read_csv( filename ):
	data = []

	with open( filename ) as f:
		reader = csv.reader( f )
		next( reader )

		for row in reader:
			data.append( row )
	return data

def calculate_mean( numbers ):
	s = sum( numbers )
	N = len( numbers )

	mean = s / N

	return mean

def calculate_median( numbers ):

	numbers = sorted( numbers )
	N = len( numbers )
	
	if N % 2 == 0:
		m1 = numbers[ int( N / 2 ) - 1 ]
		m2 = numbers[ int( N / 2 ) - 1 ]

		median = ( m1 + m2 ) / 2
	else:
		median = numbers[ int( ( N + 1 ) / 2 ) ]

	return median

def calculate_mode( numbers ):
	numbers_freq = collections.Counter( numbers ).most_common()
	max_count = numbers_freq[ 0 ][ 1 ]

	modes = []

	for num in numbers_freq:
		if num[1] == max_count:
			modes.append( num[ 0 ] )
	return modes

def find_differences( numbers ):
	mean = calculate_mean( numbers )

	diff = []

	for num in numbers:
		diff.append( num - mean )

	return diff

def calculate_variance( numbers ):
	diff = find_differences( numbers )

	squared_diff = []

	for num in diff:
		squared_diff.append( num ** 2 )

	sum_squared = sum( squared_diff )

	variance = sum_squared / len( numbers )

	return variance

def calculate_standard_deviation( numbers ):
	variance = calculate_variance( numbers )

	return variance ** .5

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

def display_stats( numbers ):
	print( 'Mean: {0}'.format( calculate_mean( numbers ) ) )
	print( 'Median: {0}'.format( calculate_median( numbers ) ) )
	print( 'Mode: {0}'.format( calculate_mode( numbers ) ) )
	print( 'Variance: {0}'.format( calculate_variance( numbers ) ) )
	print( 'Standard Deviation: {0}'.format( calculate_standard_deviation( numbers ) ) )

if __name__ == '__main__':
	cwd = os.getcwd()

	values = read_csv( cwd + '\\ch_03\\data\\data2.txt' )

	x = []
	y = []

	for line in values:
		x.append( int( line[ 0 ] ) )
		y.append( int( line[ 1 ] ) )

	try:
		correl = find_corr_x_y( x, y )
		print( correl )
	except ValueError as e:
		print( e )

	display_stats( x )