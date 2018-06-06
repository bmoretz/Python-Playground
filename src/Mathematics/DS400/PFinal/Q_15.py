from sympy import symbols, solve, diff, pprint, integrate

# After a long​ study, tree scientists conclude that a eucalyptus tree will grow at the rate of

t = symbols( 't' )
R = 0.6 + 4 / ( t + 3 ) **3
#  feet per​ year, where t is the time​ (in years).
pprint( R )

# Find the number of feet that the tree will grow in the second year.
a, b = 1, 2
round( integrate( R, ( t, a, b ) ), 3 ) # Round to three decimal places as​ needed.

# Find the number of feet that the tree will grow in the second year.
a, b = 2, 3
round( integrate( R, ( t, a, b ) ), 3 ) # Round to three decimal places as​ needed.