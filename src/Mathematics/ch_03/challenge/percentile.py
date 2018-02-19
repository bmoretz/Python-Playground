import csv
import math
import os

def read_csv( filename ):
	data = []

	with open( filename ) as f:
		reader = csv.reader( f )
		next( reader )

		for row in reader:
			if len( row ) == 0: continue

			data.append( row )
	return data

def percentile( p, data ):
	N = len( data ) + 1
	sorted( data )

	i = ( ( N * p ) / 100 ) + .5 

	if isinstance( i, int ):
		return data[ i ]
	else:
		f, k = math.modf( i )
		return ( 1 - f ) * data[ int( k ) ] + f * data[ int( k ) + 1 ]

if __name__ == '__main__':
	cwd = os.getcwd()

	values = read_csv( cwd + '\\ch_03\\data\\scores.txt' )

	scores = []

	for val in values:
		scores.append( int( val[ 0 ] ) )

	percentile( 95, scores )