# The standard normal probability function is used to describe many different populations. 
# Its graph is the​ well-known normal curve. This function is defined below. Give the intervals where the functions is increasing and decreasing.

# f(x) = 1 / sqrt( 3*pi ) e ^ -x^2/2

from sympy import *
from sympy.plotting import *

init_printing()

g_xlim = [ -4, 4 ]
g_ylim = [ 0, .5 ]
g_title = 'Standard Normal'

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

x = symbols( 'x' )

F = ( 1 / ( 3*pi ) ** .5 ) * exp( ( -x**2 / 2 ) )
dF = diff( F, x )

dis = discriminant( dF )

p = plot( F, line_color = 'B', xlim = g_xlim, ylim = g_ylim, title = g_title, show = False )

if dis < 0:
	p2 = plot( dF, line_color = 'R', title = 'Continuous', show = False )
	p.append( p2[ 0 ] )
else:
	critical_numbers = solve( dF, x )
	x2 = symbols( 'x2' )
	for c in critical_numbers:
		p_c = plot_implicit( Eq( x2, c ), title = 'Intercept', line_color = 'R', show = False )
		p.append( p_c[ 0 ] )

p.legend = True
p.show()