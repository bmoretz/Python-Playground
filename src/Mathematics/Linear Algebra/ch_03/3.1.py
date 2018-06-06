from sympy import Matrix
import numpy as np

x1 = np.array( [ 1, 4, 2 ] )
x1 = x1[ np.newaxis ]

print( x1.T )

x2 = np.array( [ 0, 3, 3 ] )
x2 = x2[ np.newaxis ]

print( x2.T )

