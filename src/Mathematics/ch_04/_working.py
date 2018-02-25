from sympy import Symbol

x = Symbol( 'x' )

x + x + 1

x.name

a = Symbol( 'x' )
a.name

from sympy import symbols

x,y,z = symbols( 'x,y,z' )

x = Symbol( 'x' )
y = Symbol( 'y' )

s = x*y + x*y

s

p = ( x + 2) * ( x + 3 )
p

x = Symbol( 'x' )
y = Symbol( 'y' )

from sympy import factor, expand
expr = x**2 - y**2

factor( expr )

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor( expr )

factors

expand( factors )

expr = x + y + x*y
factor( expr )

expr = x*x + 2*x*y + y*y
print( expr )

from sympy import pprint

pprint( expr )

expr = x**2 + 2*x*y + y**2

pprint( expr )

expr = 1 + 2*x + 2*x**2
pprint( expr )

from sympy import init_printing
init_printing( order = 'rev-lex' )
pprint( expr )

expr = x*x + x*y + x*y + y*y
res = expr.subs( {x:1-y } )
res

from sympy import simplify
expr = x*x + x*y + x*y + y*y
expr_subs = expr.subs( {x:1-y } )
simplify( expr_subs )

