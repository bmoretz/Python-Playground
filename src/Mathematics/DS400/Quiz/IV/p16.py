import math
from functools import reduce
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCr( n,r ):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

# A container contains 12 diesel engines. 
# The company chooses 4 engines at​ random, and will not ship the container if any of the engines chosen are defective. 
# 
# Find the probability that a container will be shipped even though it contains 2 defective engines.

engine_count = 12
engine_sample = 4

engine_defective = 2

no_not_defective = engine_count - engine_defective 

prob = nCk( no_not_defective, engine_sample ) / nCk( engine_count, engine_sample )

round( prob, 3 )