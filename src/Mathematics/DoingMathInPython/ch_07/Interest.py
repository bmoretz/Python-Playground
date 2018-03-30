from sympy import Symbol, Limit, S
n = Symbol( 'n' )
Limit( ( 1 + 1/n) ** n, n, S.Infinity ).doit()

# Compound Interest
p = Symbol( 'p', positive = True )
r = Symbol( 'r', positive = True )
t = Symbol( 't', positive = True )
Limit( p * ( 1 + r/n ) **  ( n*t ), n, S.Infinity ).doit()