# Suppose the total cost​ C(x) (in​ dollars) to manufacture a quantity x of weed killer​ (in hundreds of​ liters) is given by the function
# C(x) = x^3 - 3*x^2 + 8*x + 50

# Where is​ C(x) decreasing?

# Where is​ C(x) increasing?

from sympy import *
from sympy.plotting import (plot, plot_parametric,
                            plot3d_parametric_surface, plot3d_parametric_line,
                            plot3d)

init_printing()

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

x = symbols( 'x' )

C = x**3 - 3*x**2 + 8*x + 50
dC = diff( C, x )

critical_numbers = solve( dC, x )

p = plot( visible = False )

p[1] = C
p[2] = dC

p.show()