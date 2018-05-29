from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, pprint )
import matplotlib.pyplot as plt
import numpy as np

# The probability density function of a random variable on the interval [16, 25]

x = symbols( 'x' )
F = ( 3/122 ) * sqrt( x )

a, b = 16, 25

def expected_value( f, var, a, b ):
	return integrate( var * f, ( var, a, b ) )

def variance( f, var, a, b, mu ):
	return integrate( ( ( var **2 ) * f ), ( var, a, b ) ) - mu**2

def std_dev( var ):
	return sqrt( var )

# Find the expected value.
ev = expected_value( F, x, a, b )
round( ev, 2 )

# Find the variance.
variance = variance( F, x, a, b, ev )
round( variance, 2 )

# Find the standard deviation.
stdev = std_dev( variance )
round( stdev, 2 )

# Find the probability that the random variable has a value greater than the mean.
prob_gt_mean = integrate( F, ( x, ev, b ) )
round( prob_gt_mean, 2 )

# find the probability that the value of the random variable is within one standard deviation of the mean.
prob_within_1sd = integrate( F, ( x, ev - stdev, ev + stdev ) )
round( prob_within_1sd, 2 )