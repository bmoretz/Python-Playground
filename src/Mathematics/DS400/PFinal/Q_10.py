from sympy import ( symbols, diff, pprint, simplify )

x = symbols( 'x' )
F = ( x**3 - 8 ) ** (2/3)

pprint( F )

pprint( simplify( diff( F, x ) ) )