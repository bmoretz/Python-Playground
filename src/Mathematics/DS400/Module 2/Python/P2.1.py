from sympy import symbols, plot_implicit, plot, plot_parametric
from sympy.plotting import plot_parametric

x, y = symbols( 'x, y' )


exprs = [[ -3*x + 4*y >= 12, 'b' ],
		 [ x + 3*y >= 6, 'r'],
		 [ y <= 1, 'g']]

p = plot_implicit( exprs[ 0 ][ 0 ], line_color = exprs[ 0 ][ 1 ], show = False )

p.extend( plot_implicit( exprs[ 1 ][ 0 ], line_color = exprs[ 1 ][ 1 ], show = False ) )

p.extend( plot_parametric( x, 1, line_color = exprs[ 2 ][ 1 ], show = False ) )

p.show()
