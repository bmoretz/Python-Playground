# The total profit P(x) (in thousands of dollars) from the sale of x units of a certain perscription drug is given by the function:
# P(x) = ln( -x**3 + 3*x + 72*x + 1 )

from sympy import *
from sympy.plotting import (plot, plot_parametric,
                            plot3d_parametric_surface, plot3d_parametric_line,
                            plot3d)

init_printing()

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

x = symbols( 'x' )

P = ln( -x**3 + 3*x**2 + 72*x + 1 )
dP = simplify( diff( P, x ) )
ddP = simplify( diff( dP, x ) )

critical_numbers = solve( dP, x )
critical_numbers = solve( ddP, x )

disp_fun( dP )

critical_numbers

p = plot( P, show=False ) 
p.show()
