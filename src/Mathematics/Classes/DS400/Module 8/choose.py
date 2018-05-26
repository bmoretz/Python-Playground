# Kristen's financial advisor has given her a list of 12 potential investments and has asked her to select and rank her favorite four. 
# 
# In how many different ways can she do​ this?

import math
from functools import reduce
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

def perm( n,k ): 
  return math.factorial( n ) / math.factorial( n - k )

perm( 12, 4 )