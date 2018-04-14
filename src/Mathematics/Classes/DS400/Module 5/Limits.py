from sympy import symbols, Limit, S, pprint

t = symbols( 't' )
pT = ( 3800 * t ) / ( t + 3 )
lim = Limit( pT, t, S.Infinity )

pprint( lim.doit() )

546 * 3.25