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

flights = 42
prob = .88

all_flights = nCk( flights, flights ) * prob**flights * ( 1 - prob ) ** ( flights - flights )
round( all_flights, 4 )

# The probability that between 36 and 38 ​flights, inclusive, are on time is:

a = nCk( flights, 36 ) * prob**36 * ( 1 - prob ) ** ( flights - 36 )
b = nCk( flights, 37 ) * prob**37 * ( 1 - prob ) ** ( flights - 37 )
c = nCk( flights, 38 ) * prob**38 * ( 1 - prob ) ** ( flights - 38 )

round( a + b + c, 4 )
