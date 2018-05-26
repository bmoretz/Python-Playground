import math
from functools import reduce
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

# A legislative committee consists of 7 Democrats and 8 Republicans. 
# A delegation of 4 is to be selected to visit a small island republic. Complete parts​ (a) through​ (d) below.

# How many different delegations are​ possible?
nCk( 7 + 8, 4 )

# How many delegations would have all​ Democrats?
nCk( 7, 4 )

# How many delegations would have 3 Democrats and 1​ Republican?
nCk( 7, 3 ) * nCk( 8, 1 )

# How many delegations would include at least 1​ Republican?
nCk( 7 + 8, 4 ) - nCk( 7, 4 )