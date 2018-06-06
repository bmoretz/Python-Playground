'''
Even-Odd Vending Machine
'''

def even_odd_vm( num ):

		switch = -1

		if num % 2 == 0:
			print( "Even Chosen" )
			switch = 0
		else:
			print( "Odd Chosen." )
			switch = 1

		print( num )
		print( "Next 9... " )

		index = 1;
		for i in range( num + 1, num + 19 ) :
			if( i % 2 == switch ) :
				print( "{0}:{1}".format( index, i ) )
				index = index + 1

if __name__ == '__main__':
	try:
		num = int( input( "Please enter your number: " ) )
		even_odd_vm( num )
	except ValueError:
		print( "Invalid Number." )