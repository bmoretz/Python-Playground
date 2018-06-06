from sympy import Matrix, pprint

M = Matrix( [
	[	1,		0,	1, 0, 0, 0, 0, 0, 3 ],
	[	0,		1,	0, 1, 0, 0, 0, 0, 4 ],
	[	2,		1,	0, 0, 1, 0, 0, 0, 7 ],
	[	1,		1,	0, 0, 0, 1, 0, 0, 5 ],
	[  -1,		0,	0, 0, 0, 0, 1, 0, 0 ],
	[   0,		-1,	0, 0, 0, 0, 0, 1, 0 ],
	[-3000,	-2000,	0, 0, 0, 0, 0, 0, 0 ] ] )

pprint( M )

# Pivot 1

[ M[i,8]/M[i,0] for i in range(0,4) ]

M.row_op( 2, lambda v,j: v-2*M[ 0, j ] )
M.row_op( 3, lambda v,j: v-1*M[ 0, j ] )
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