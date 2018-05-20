from sympy import *

# A mailing service places a limit of 66 in. on the combined length and girth of​ 
# (distance around) a package to be sent parcel post. 
# 
# What dimensions of a rectangular box with square​ cross-section will contain the largest 
# volume that can be​ mailed? (Hint: There are two different​ girths.)

L = 42
x = symbols( 'x', positive = True )

V = x**2 * ( L - 4*x )
dV = diff( V, x )

max_x = solve( dV, x )[ 0 ]

print( 'Dim {0}, {1}'.format( max_x, max_x * 2 ) )