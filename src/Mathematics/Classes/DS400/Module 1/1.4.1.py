import numpy as np
from prettytable import PrettyTable

def ptable( t ):
	p = PrettyTable()
	for row in t:
		p.add_row( row )

	print( p.get_string( header = False, border = False ) )

C = np.array( [[ 22, 25, 38 ], [ 31, 34, 35 ]] )
K = np.array( [[ 5, 10, 8 ], [ 11, 14, 15 ]] )

R = C - K

# Results
ptable( R )

# 1.) Row 2
R[1,:]

# 2.) Col 3
R[:,2]

# Common Element
R[ R[:,0] == R[:,1] ]