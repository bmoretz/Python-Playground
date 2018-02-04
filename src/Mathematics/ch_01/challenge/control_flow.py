'''
Run until exit layout
'''

def fun():
	print( 'I am in an endless loop' )

if __name__ == '__main__':
	while True:
		fun()
		answer = input( 'Do you want to exit? (y) for yes ' )
		if answer == 'y':
			break;