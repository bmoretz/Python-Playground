from sympy import symbols, sympify, factor, pprint, init_printing, plot, solve
from sympy.core import SympifyError

init_printing( order = 'rev-lex' )

x, y = symbols( 'x, y' )

expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12

expr1 = sympify( expr1 )
expr2 = sympify( expr2 )

expr1_sln = solve( expr1, y ) 
expr2_sln = solve( expr2, y )

p = plot( expr1_sln[ 0 ], expr2_sln[ 0 ], legend = True, show = False )

p[ 0 ].line_color = 'b'
p[ 1 ].line_color = 'r'

sln = solve( ( expr1, expr2 ), symbols( 'x, y' ) )

pprint( sln )

p.show()