# A company plans to enclose three parallel rectangular areas for sorting returned goods. 
# The three areas are within one large rectangular area and 1400 yd of fencing is available. What is the largest total area that can be​ enclosed?

from sympy import symbols, solve, diff

x, y = symbols( 'x y', positive = True )

A = 2*x + 4*y - 976

y_eq = solve( A, y )[ 0 ]

Ax = y_eq * x

dA = diff( Ax, x )

crit_val = solve( dA, x )[ 0 ]
short_side = y_eq.subs( { x: crit_val } )
total_area = Ax.subs( { x: crit_val } )

if __name__ == '__main__':
	print( 'Shorter Len: {0} yd'.format( short_side ) )
	print( 'Longer side: {0} yd'.format( crit_val ) )
	print( 'Total Area: {0} yd^2'.format( total_area ) )