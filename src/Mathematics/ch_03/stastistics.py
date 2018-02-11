from collections import Counter

def calculate_mean( numbers ):
	s = sum( numbers )
	N = len( numbers )

	# mean
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
	numbers_freq = Counter( numbers ).most_common()
	max_count = numbers_freq[ 0 ][ 1 ]

	modes = []

	for num in numbers_freq:
		if num[1] == max_count:
			modes.append( num[ 0 ] )
	return modes

def freqency_table( numbers ):
	table = Counter( numbers )
	numbers_freq = table.most_common()
	numbers_freq.sort()

	for number in numbers_freq:
		print( '{0}\t{1}'.format( number[ 0 ], number[ 1 ] ) )

if __name__ == '__main__':

	donations = [ 100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200 ]

	mean = calculate_mean( donations )
	median = calculate_median( donations )
	mode = calculate_mode( donations )

	N = len( donations )

	print( 'Mean donation over the last {0} days is {1}'.format( N, mean ) )
	print( 'Median donation over the last {0} days is {1}'.format( N, median ) )
	print( 'Most common donation over the last {0} days is {1}'.format( N, mode ) )