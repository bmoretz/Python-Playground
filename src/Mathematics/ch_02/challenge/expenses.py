'''
Expenses Chart
'''

import matplotlib.pyplot as plt

def create_bar_chart( data, labels ):
	# Number of bars
	num_bars = len( data )
	
	# This list is the point on yhe y-axis where each
	# Bar is centered. Here it will be [1, 2, 3...]
	positions = range( 1, num_bars + 1 )
	plt.barh( positions, data, align = 'center' )
	
	# set labels for each bar
	plt.yticks( positions, labels )
	plt.ylabel( 'Categories' )
	plt.xlabel( 'Amount' )
	plt.title( 'Weekly Expenditures' )

	# Turns on grid which may assist in visual estimation

	plt.grid()
	plt.show()

if __name__ == '__main__':

	category = []
	expend = []
	
	num_categories = int( input( 'Enter the number of categories: ' ) )

	count = 0
	while count < num_categories:
		category.append( input( "Enter category: " ) )
		expend.append( int( input( "Expenditure: " ) ) )
		count = count + 1

	create_bar_chart( expend, category )