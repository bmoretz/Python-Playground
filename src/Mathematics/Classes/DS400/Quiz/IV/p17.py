import math
from functools import reduce
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

# According to an​ airline, a particular flight is on time 88​% of the time. 
# Suppose 42 flights are randomly selected and the number of on time flights is recorded. 
# 
# Find the probabilities of the following events occurring.

# The probability that all 42 flights are on time is

flights = 37
prob = .91

all_flights = nCk( flights, flights ) * prob**flights * ( 1 - prob ) ** ( flights - flights )
round( all_flights, 4 )

# The probability that between 30 and 32 ​flights, inclusive, are on time is:

n_a = 30
a = nCk( flights, n_a ) * prob**n_a * ( 1 - prob ) ** ( flights - n_a )

n_b = 31
b = nCk( flights, n_b ) * prob**n_b * ( 1 - prob ) ** ( flights - n_b )

n_c = 32 
c = nCk( flights, n_c ) * prob**n_c * ( 1 - prob ) ** ( flights - n_c )

round( a + b + c, 4 )
