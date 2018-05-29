from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, ln, pprint, oo )

# The lifetime of a printer costing ​$200 is exponentially distributed with mean 5 years. 
# The manufacturer agrees to pay a full refund to a buyer if the printer fails during the first year following its​ purchase, and a​ one-half refund if it fails during the second year. 
# If the manufacturer sells 100 printers​, how much should it expect to pay in​ refunds?

cost = 100

mu = 3
a = 1 / mu
x = symbols( 'x' )

pdf = a * exp( -x / mu )

year_1 = integrate( pdf, ( x, 0, 1 ) ).evalf()
year_2 = integrate( pdf, ( x, 1, 2 ) ).evalf()

refund = year_1 * cost + year_2 * ( .5 * cost ) 
refund = refund * 100

round( refund, 2 ) 