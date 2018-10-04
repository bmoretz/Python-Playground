import math
from functools import reduce
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

import operator as op

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

# A lottery game requires that you pick 8 different numbers from 1 to 75. 
# If you pick all 7 winning​ numbers, you win the jackpot. 
# If you pick 6 of the 7 numbers​ correctly, you win ​$250,000. 
# 
# In how many ways can you pick exactly 6 of the 7 winning numbers without regard to​ order?

n, r, c = 7, 6, 75

nCr( n, r ) * ( c - n )