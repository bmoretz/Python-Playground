filename = 'data/points.txt'

in_file = open( filename, 'r' ) # Open file for reading
line = in_file.readline() # Read first line

# Read x and y coordinates from the file and store in list

x = []
y = []

for line in in_file:
	words = line.split()
	x.append( float( words[ 0 ] ) )
	y.append( float( words[ 1 ] ) )
in_file.close()

