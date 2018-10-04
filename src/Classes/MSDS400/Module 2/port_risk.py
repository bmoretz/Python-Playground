# Minimize x1*x4( x1 + x2 + x3 ) + x3
# s.t.
# x1 * x2 * x3 * x4 >= 25
# x1**2 + x2**2 + x3**2 + x4**2 = 40
# 1 <= x1, x2, x3, x4 <= 5
# x0 = ( 1, 5, 5, 1 )

import numpy as np
from scipy.optimize import minimize
from sympy import plot

def objective( params ):

	s, h = params

	return 3*s + 2*h

# for every 3 units of security A, we need 1 unit of security C.
def hedge_constraint_a( params ):

	s, h = params

	return 3*a - c

def total_vol_constraint( params ):

	s, h = params
	
	return a + - 100

con_hedge = { 'type' : 'eq', 'fun': hedge_constraint_a }
con_vol = { 'type' : 'ineq', 'fun': total_vol_constraint }

cons = [ con_hedge, con_vol ]

b = ( 1.0, 10.0 )
bnds = ( b, b, b, b )

initial = [ 1, 1, 1 ]

result = minimize( objective, x0=initial, \
	constraints = cons )

if result.success:
	print( result )
else:
	raise ValueError( result.message )