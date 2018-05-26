# A recent study found that 85​% of​ breast-cancer cases are detectable by mammogram. 
# Suppose a random sample of 12 women with breast cancer are given mammograms. 
#
# Find the probability that all of the cases are​ detectable, assuming that detection in the cases is independent.

pS = 0.85
places = 4
n = 12

# Binomial Probablility
def nCk(n,k): 
  return int( reduce( mul, ( Fraction( n-i, i+1 ) for i in range( k ) ), 1) )

def binomial_prob( n, x, pS ):
	return round( nCk( n, x ) * pS ** x * ( 1 - pS ) ** ( n - x ), places )

binomial_prob( n, n, pS )