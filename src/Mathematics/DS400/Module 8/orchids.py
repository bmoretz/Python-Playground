# 7  orchids from a collection of 20 are to be selected for a flower show. Complete parts​ (a) and​ (b) below.

import math
from functools import reduce
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, ( Fraction( n - i, i+ 1) for i in range( k ) ), 1) )

# In how many ways can this be​ done?
nCk( 20, 7 )

# How many ways can the 7 be selected if 2 special plants from the 20 must be​ included?
nCk( 18, 5 )