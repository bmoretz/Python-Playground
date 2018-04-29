from sympy import Matrix
import numpy as np
import math

# np.dot
def dot_prod( a, b ):
	
	prod = 0
	for i in range( 1, len( a ) ):
		prod += a[ i ] * b[ i ]
	return prod

# np.cross
def cross_prod( a, b ):
	return np.array( [ a[1]*b[2] - a[2]*b[1], \
					   a[2]*b[0] - a[0]*b[2], \
					   a[0]*b[1] - a[1]*b[0] ] )

def magnitude( v ):
	return math.sqrt( dot_prod( v, v ) )

# 2.5

# Given:
u = np.array( [ 1, 1, 0 ] )
v = np.array( [ 0, 0, 3 ] )

# a
v + u

# b
u - v

# c
3*u + v

# d
magnitude( u )

# 2.5

# Given:
v = np.array( [ 1, 2, 3 ] )
w = np.array( [ 0, 1, 1 ] )

# a
dot_prod( v, w )

# b
cross_prod( v, w )

# c
cross_prod( w, v )

# d
cross_prod( w, w )

# 2.6

