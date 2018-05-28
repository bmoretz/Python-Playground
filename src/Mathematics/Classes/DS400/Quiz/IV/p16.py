import math
from functools import reduce
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

def perm( n,k ): 
  return math.factorial( n ) / math.factorial( n - k )

# A container contains 10 diesel engines. 
# The company chooses 8 engines at​ random, and will not ship the container if any of the engines chosen are defective. 
# 
# Find the probability that a container will be shipped even though it contains 2 defective engines.

prob = nCk( 8, 8 ) / nCk( 10, 8 )

round( prob, 3 )