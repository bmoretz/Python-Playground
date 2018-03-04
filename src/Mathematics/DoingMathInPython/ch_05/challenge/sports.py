import os
import csv

from matplotlib import pyplot as plt
from sympy import FiniteSet
from matplotlib_venn import vinn2, venn2_circles

def read_csv( fileName ):
	football = []
	others = []

	with open( fileName ) as f:
		reader = csv.reader( f )
		next( reader )
		for row in reader:
			if row[ 1 ] == '1':
				football.append( row[ 0 ] )
			if row[ 2 ] == '1':
				others.append( row[ 0 ] )
	return football, others


if __name__ == '__main__':
	cwd = os.getcwd()

	football, others = read_csv( cwd + '\\DoingMathInPython\\ch_05\\data\\football.txt' )

	v = vinn2( football, others )