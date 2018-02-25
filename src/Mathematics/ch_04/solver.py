from sympy import symbols, solve, pprint

x = Symbol( 'x' )

expr = x - 5 - 7

solve( expr )

expr = x**2 + 5*x + 4
solve( expr )

s, u, t, a = symbols( 's, u, t, a' )

expr = u * t + ( 1 / 2 ) * a * t * t - s

t_expr = solve( expr, t, dict = True )

pprint( t_expr )

x, a, b, c = symbols( 'x, a, b, c' )
expr = a*x*x + b*x + c
sln = solve( expr, x, dict = True )

pprint( sln )

# System of Equations

x = Symbol( 'x' )
y = Symbol( 'y' )

expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12

soln = solve( ( expr1, expr2 ), dict = True )

soln = soln[ 0 ]

expr1.subs( {x:soln[ x ], y: soln[ y ] } )
expr2.subs( {x:soln[ x ], y: soln[ y ] } )
