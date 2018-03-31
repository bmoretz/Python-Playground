from sympy import symbols, solve, sympify

t = symbols( "t" )

expr = 5*t**2 + 10

expr = sympify( expr )

soln = solve( expr, t, dict = True )

soln = soln[ 0 ]