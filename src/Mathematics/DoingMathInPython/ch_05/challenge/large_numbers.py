import random

sides = 6

def roll():
	return random.randint( 1, sides )


def expected_value( values ):
	p = 1 / len( values )
	
	print( len( values ) )

	ev = 0
	index = 0
	
	for value in values:
		ev += value * p

	return ev

def run_trial( num_trials ):

	rolls = []
	
	for num in range( 0, num_trials ):
		rolls.append( roll() )
	
	n = len( rolls )

	print( 'Trials: {0}, Trial Average: {1}'.format( n, sum( rolls ) / n ) )

if __name__ == '__main__':

	values = range( 1, sides + 1 )

	ev = expected_value( values )
	print( 'Expected Value: {0}'.format( ev ) )

	run_trial( 100 )
	run_trial( 1000 )
	run_trial( 10000 )
	run_trial( 50000 )