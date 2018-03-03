from sympy import FiniteSet, pi

def time_period( length, g ):
	T = 2*pi**( length / g ) ** 0.5
	return T

L = FiniteSet( 15, 18, 21, 22.5, 25 )
G = FiniteSet( 9.8, 9.78, 9.83 )

def display_table( l_values, g_values ):

	print( '{0:^15}{1:^15}{2:^15}'.format( 'Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)' ) )

	for elem in l_values*g_values:
		l = elem[ 0 ]
		g = elem[ 1 ]
		t = time_period( l / 100, g )
	
		print( '{0:^15}{1:^15}{2:^15}'.format( float( l ), float( g ), float( t ) ) )

display_table( L, G )`