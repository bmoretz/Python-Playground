from sympy import ( symbols, diff, pprint )

x = symbols( 'x' )
F = ( x**3 - 8 ) ** (2/3)

pprint( F )

pprint( diff( F, x ) )

