
# A rectangular tank with a square​ base, an open​ top, and a volume of 500 ft cubed is to be constructed of sheet steel. 
# Find the dimensions of the tank that has the minimum surface area.

from sympy import symbols, solve, diff, pprint

volume = 6912

s, h = symbols( 's, h' )
A = s**2 + 4*s*h
V = s**2 * h

H = solve( V - volume, h )[ 0 ]

pprint( H )

Ah = A.subs( { h: H } ).evalf()

dA_ds = diff( Ah, s )

min_side = solve( dA_ds, s )[ 0 ]
min_height = H.subs( { s: min_side } ).evalf()

if __name__ == '__main__':
	print( 'The dimensions of the tank with the minimum surface area are: ' )
	print( 'Min side: {0:.0f} ft x {0:.0f} ft x {1:.0f} ft'.format( min_side, min_height ) )
	print( '{0:.0f}, {0:.0f}, {1:.0f}'.format( min_side, min_height ) )