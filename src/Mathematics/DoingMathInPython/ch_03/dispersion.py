
def find_range( numbers ):
	loweset = min( numbers )
	highest = max( numbers )

	rng = highest - loweset

	return loweset, highest, rng

def calculate_mean( numbers ):
	s = sum( numbers )
	N = len( numbers )

	# mean
	mean = s / N

	return mean

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

if __name__ == '__main__':

	donations = [ 100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200 ]

	low, high, rng = find_range( donations )
	print( 'Lowest {0}, Highest {1}, Range {2}'.format( low, high, rng ) )

	variance = calculate_variance( donations )
	print( 'The variance of the list is {0}'.format( variance ) )

	stdev = calculate_standard_deviation( donations )
	print( 'The standard deviation of the list is {0}'.format( stdev ) )