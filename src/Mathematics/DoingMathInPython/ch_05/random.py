'''
Roll a die until the total score is 20
'''

import matplotlib.pyplot as plt
import random

def roll():
	return random.randint( 1, 6 )

target_score = 20

if __name__ == '__main__':

	score = 0
	num_rolls = 0

	while score < target_score:
		die_roll = roll()
		num_rolls += 1
		score += die_roll
		print( 'Rolled: {0}'.format( die_roll ) )

	print( 'Score of {0} reached in {1} rolls.'.format( score, num_rolls ) )