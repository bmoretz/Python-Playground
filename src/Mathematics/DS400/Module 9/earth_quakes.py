from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, pprint )
import matplotlib.pyplot as plt
import numpy as np

# The time between major earthquakes in the Taiwan region is a random variable with probability density function:
t = symbols( 't' )
F = 1 / ( 3650.1 * exp( -t / 3650.1 ) )

def years_to_days( years ):
	return years * 365

a, b, c = years_to_days( 2 ), years_to_days( 6 ), 3650.1 
fX = -1 * ( exp( -b/c ) - exp(-a/c) )
round( fX, 2 )

a, b, c = 0, 5110, 3650.1 
fX = -1 * ( exp( -b/c ) - exp(-a/c) )
1 - round( fX, 2 )