import math
from functools import reduce
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

def perm( n,k ): 
  return math.factorial( n ) / math.factorial( n - k )

# A lottery game requires that you pick 8 different numbers from 1 to 95. 
# If you pick all 8 winning​ numbers, you win the jackpot. 
# If you pick 7 of the 8 numbers​ correctly, you win ​$250,000. 
# 
# In how many ways can you pick exactly 7 of the 8 winning numbers without regard to​ order?

nCk( 8, 7 ) * nCk( 95, 1 )