# The total profit​ P(x) (in thousands of​ dollars) from a sale of x thousand units of a new product is given by:
# P(x) = ln( -x**3 + 3*x**2 + 105*x + 1 )

from sympy import *
from sympy.plotting import ( plot, plot_parametric )

g_xlim = [ -10, 10 ]
g_ylim = [ -7, 7 ]

x = symbols( 'x' )

P = ln( -x**3 + 3*x**2 + 105*x + 1 )
dP = diff( P, x )

p = plot( P, ylim = g_ylim, xlim = g_xlim, show = False ) 

critical_numbers = solve( dP, x )

for c in critical_numbers:
	x2 = symbols( 'x2' )
	p_c = plot_implicit( Eq( x2, c ), ylim = g_ylim, xlim = g_xlim, line_color = 'R', show = False )
	p.append( p_c[ 0 ] )

p.show()