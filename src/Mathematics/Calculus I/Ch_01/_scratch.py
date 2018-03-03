from sympy import symbols, solve, sympify

expr = 5*t**2 + 10

expr = sympify( expr )
t = symbols( "t" )

soln = solve( expr, t )

soln = soln[ 0 ]

expr.subs( 