# According to a​ survey, 20.8​% of​ credit-card-holding families in a certain area hardly ever pay off the balance. 
# Suppose a random sample of 18 ​credit-card-holding families is taken. 
# 
# Find the probability that at least 4 families hardly ever pay off the balance

pS = 0.216
places = 4
n = 21

# Binomial Probablility
def nCk(n,k): 
  return int( reduce( mul, ( Fraction( n-i, i+1 ) for i in range( k ) ), 1) )

def binomial_prob( n, x, pS ):
	return round( nCk( n, x ) * pS ** x * ( 1 - pS ) ** ( n - x ), places )

p0 = binomial_prob( n, 0, pS )
p1 = binomial_prob( n, 1, pS )
p2 = binomial_prob( n, 2, pS )
p3 = binomial_prob( n, 3, pS )

1 - ( p0 + p1 + p2 + p3 )