def read_points( file_name ):

	in_file = open( file_name, 'r' ) # Open file for reading
	line = in_file.readline() # Read first line

	# Read x and y coordinates from the file and store in list

	x = []
	y = []

	for line in in_file:
		if line.startswith( '#' ):
			continue

		words = line.split()
		x.append( float( words[ 0 ] ) )
		y.append( float( words[ 1 ] ) )

	in_file.close()

	return x, y

def write_points( x, y ):
	out_file = open( file_name, 'w' ) # Open file for writing
	out_file.write( '# x and y coordinates\n' )

	for xi, yi in zip( x, y ):
		out_file.write( '%10.5f %10.5f\n' % ( xi, yi ) )
	out_file.close()
