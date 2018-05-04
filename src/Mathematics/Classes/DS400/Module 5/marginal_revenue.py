# If the price in dollars of a stereo system is given by p(q) = 9000 / q**2 + 1500, 
# where q represents the demand for the​ product, find the marginal revenue when the demand is 30.

# marginal revenue = R( q ) = pq

from sympy import *

p, q = symbols( 'p,q' )

revUnits = 30

fP = ( 9000 / q**2 ) + 1500

rQ = fP * q

dQ = Derivative( rQ, q ).doit()

margRev = dQ.subs( { q: revUnits } )

pprint( fP )

print( 'marginal revenue when q = {0} is {1}'.format( revUnits, margRev ) )