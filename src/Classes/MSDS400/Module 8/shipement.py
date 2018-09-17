# A shipment of 9 printers contains 2 that are defective. 
# 
# Find the probability that a sample of size 2​, drawn from the 9​, will not contain a defective printer.

from functools import reduce
from operator import mul
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, ( Fraction( n-i, i+1 ) for i in range(k) ), 1) )

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numer, denom):

    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if reduced_den == 1:
        return "%d/%d is simplified to %d" % (numer, denom, reduced_num)
    elif common_divisor == 1:
        return "%d/%d is already at its most simplified state" % (numer, denom)
    else:
        return "%d/%d is simplified to %d/%d" % (numer, denom, reduced_num, reduced_den)

n = nCk( 7, 2 ) # choices of non defective
k = nCk( 9, 2 ) # total choices

simplify_fraction( n, k )