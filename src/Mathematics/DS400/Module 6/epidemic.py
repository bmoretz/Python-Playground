# The number of people P(t) (in hundreds) infected t days after an epidemic begins is approximated by the function:
# P(t) = 10*ln( 0.19*t + 1 ) / 0.19*t + 1

from sympy import *
from sympy.plotting import (Plot, plot, plot_parametric,
                            plot3d_parametric_surface, plot3d_parametric_line,
                            plot3d)

init_printing()

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

t = symbols( 't' )

P = 10*ln( 0.19*t + 1 ) / ( 0.19*t + 1 )
dP = simplify( diff( P, t ) )

critical_numbers = solve( dP, t )

p = plot( P, show=False ) 
p.show()