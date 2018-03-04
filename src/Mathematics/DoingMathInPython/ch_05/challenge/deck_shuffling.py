import random

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	
	def __str__(self):
		return 'Suit: {0}, Rank {1}'.format( suit, rank )

if __name__ == '__main__':

	cards = [ Card( 'spades', '10' ), Card( 'spades', 'ace' ), Card( 'jack', 'hearts' ), Card( 'king', 'diamonds' ) ]

	random.shuffle( cards )

	for card in cards:
		print( 'Suit: {0}, Rank {1}'.format( csard.suit, card.rank ) )