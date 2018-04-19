# A dietician is planning a snack package of fruit and nuts.

# Each ounce of fruit will supply 1 unit of​ protein, 2 units of​ carbohydrates, and 1 unit of fat. 
# Each ounce of nuts will supply 1 unit of​ protein, 1 unit of​ carbohydrates, and 1 unit of fat. 
# Every package must provide at least 5 units of​ protein, at least 9 units of​ carbohydrates, and no more than 8 units of fat. 
# Let x equal the ounces of fruit and y equal the ounces of nuts to be used in each package. 

# a. Write a system of inequalities to express the conditions of the problem.
# b. Graph the feasible region of the system.

from sympy import symbols, plot_implicit, plot
from sympy.plotting import plot_parametric

x_rng = 15
y_rng = 15

x, y = symbols( 'x, y' )

exprs = [[ x + y >= 5, 'b' ],
		 [ 2*x + y >= 9, 'r'],
		 [ x + y <= 8, 'g']]

p = plot_implicit( exprs[ 0 ][ 0 ], ( x, -x_rng, x_rng ), ( y, -y_rng, y_rng ),\
   line_color = exprs[ 0 ][ 1 ], show = False )

p.extend( plot_implicit( exprs[ 1 ][ 0 ], ( x, -x_rng, x_rng ), ( y, -y_rng, y_rng ),\
	line_color = exprs[ 1 ][ 1 ], show = False ) )

p.extend( plot_implicit( exprs[ 2 ][ 0 ], ( x, -x_rng, x_rng ), ( y, -y_rng, y_rng ),\
   line_color = exprs[ 2 ][ 1 ], show = False ) )

p.show()
