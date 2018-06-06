import numpy as np

# np.cross
def cross_prod( a, b ):
	return np.array( [ a[1]*b[2] - a[2]*b[1], \
					   a[2]*b[0] - a[0]*b[2], \
					   a[0]*b[1] - a[1]*b[0] ] )

i = np.array( [ 1, 0, 0 ] )
j = np.array( [ 0, 1, 0 ] )
k = np.array( [ 0, 0, 1 ] )


neg_i = -1 * i

cross_prod( neg_i, k ) + cross_prod( j, i )

cross_prod( i, i )