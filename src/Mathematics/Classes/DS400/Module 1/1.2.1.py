import matplotlib.pyplot
from matplotlib.pyplot import *

import numpy
from numpy import linspace, ndarray

import sympy
from sympy import symbols, sympify, solve

# supply & demand functions
p, q = symbols( 'p,q' )
dF = 9 - 0.75*q
sF = 0.75*q

supply_factor = 1000

def get_demand( price ):
	sln = solve( dF - price, q )[ 0 ]

	return round( sln, 2 )

def get_supply( qty ):
	sln = solve( sF - qty, q )[ 0 ] * supply_factor
	return round( sln, 2 )

def graphit():
	len = linspace( 0, 20, 50 )

	figure()

	y = []
	for x in len:
		y.append( dF.subs( { q: x } ) )

	plot( len, y )

	y = []
	for x in len:
		y.append( sF.subs( { q: x } ) )

	plot( len, y )

	legend (('cost','revenue'),loc=2)
	title( 'Breakeven Analysis' )
	show()

if __name__ == '__main__':

	# a
	price = 5.25
	print( 'demand at {0} is {1}.'.format( price, get_demand( price ) ) )

	# b
	print( 'supply at {0}: {1}'.format( price, get_supply( price ) ) )
	price = 3
	print( 'supply at {0}: {1}'.format( price, get_supply( price ) ) )

	# c
	graphit()