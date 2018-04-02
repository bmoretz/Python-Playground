from sympy import Symbol, exp, sqrt, pi, Integral, S

x = Symbol( 'x' )
# probability function ( converges around ~10 )
p = exp( -( x - 10 ) **2/2 ) / sqrt( 2 * pi )
# probability the value is between 11 and 12
Integral( p, ( x, 11, 12 ) ).doit().evalf()

# validate pdf
Integral( p, ( x, S.NegativeInfinity, S.Infinity) ).doit() # must be 1

