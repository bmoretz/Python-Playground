from sympy import Matrix
import numpy as np

M = Matrix( [ [ 1, 2, 2, 2 ], \
			[ 2, 4, 6, 8 ], \
			[ 3, 6, 8, 10 ] ] )

result = M.rref()

# Reduced Row Form
np.array( result[0].tolist(), dtype=float )

# Pivot Variables
pivots = result[ 1 ]

pivots