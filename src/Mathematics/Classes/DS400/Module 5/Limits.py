from sympy import symbols, Limit, S, pprint

t = symbols( 't' )
pT = .37 +  .21*t
lim = Limit( pT, t, S.Infinity )

pprint( lim.doit() )

x = symbols('x')
fx = .37 + .21*x
fx.subs( { x: 2.99999} )

.37 + .21 + .21