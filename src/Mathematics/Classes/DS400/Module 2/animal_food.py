# An animal food must provide 60 units of vitamins and 65 calories per serving. 
# One gram of soybean meal provides 2.5 units of vitamins and 5 calories. 
# One gram of meat byproducts provides 4.5 units of vitamins and 3 calories. 
# One gram of grain provides 5 units of vitamins and 10 calories. 
# A gram of soybean meal costs 8 ​cents, a gram of meat byproducts 9 ​cents, and a gram of grain 10 cents. Complete parts​ (a) and​ (b) below.

from sympy import Matrix, pprint

M = Matrix( [
	[ 2.5,		5,		1, 0, 0, 0, 6 ],
	[ 4.5,		3,		0, 1, 0, 0, 9 ],
	[ 5,		10,		0, 0, 1, 0, 10 ],
	[ -60,		-65,	0, 0, 0, 1, 0 ] ] )

pprint( M )

# Pivot 1

[ M[ i, M.cols - 1 ] / M[ i,0 ] for i in range( 0, M.rows ) ]

M.row_op( 0, lambda v,j: 2*v-M[ 2, j ] )
M.row_op( 3, lambda v,j: v-1*M[ 0, j ] )

pprint( M )


M.row_op( 4, lambda v,j: v+1*M[ 0, j ] )
M.row_op( 6, lambda v,j: v+3000*M[ 0, j ] )

pprint( M )

# Pivot 2
[ M[i,8]/M[i,1] for i in range(0,4) ]

M.row_op( 1, lambda v,j: v-1*M[2,j] )
M.row_op( 3, lambda v,j: v-1*M[2,j] )
M.row_op( 5, lambda v,j: v+1*M[2,j] )
M.row_op( 6, lambda v,j: v+2000*M[2,j ] )

pprint( M )

# Pivot 3
[ M[i,8]/M[i,2] for i in range(0,4) ]

M.row_op(0, lambda v,j: v-1*M[3,j] )
M.row_op(1, lambda v,j: v-2*M[3,j] )
M.row_op(2, lambda v,j: v+2*M[3,j] )
M.row_op(4, lambda v,j: v-M[3,j] )
M.row_op(5, lambda v,j: v+2*M[3,j] )
M.row_op(6, lambda v,j: v+1000*M[3,j] )

pprint( M )

