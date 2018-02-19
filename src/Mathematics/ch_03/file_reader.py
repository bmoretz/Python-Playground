import os
import csv

def read_csv( filename ):
	data = []

	with open( filename ) as f:
		reader = csv.reader( f )
		next( reader )

		for row in reader:
			data.append( row )
	return data

if __name__ == '__main__':
	cwd = os.getcwd()

	read_csv( cwd + '\\ch_03\\data\\mydata.txt' )