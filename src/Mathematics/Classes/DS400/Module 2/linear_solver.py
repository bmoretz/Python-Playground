from scipy.optimize import linprog

c = [-3000, -2000]

A = [[ 1, 0 ],
	 [ 0, 1 ],
	 [ 2, 1 ],
	 [ 1, 1 ],
	 [ -1, 0 ],
	 [ 0, -1 ]]

b = [ 3, 4, 7, 5, 0, 0 ]

linprog( c, A_ub = A, b_ub=  b )

help(linprog)