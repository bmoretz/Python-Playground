# The cost function for q units of a certain item is:

# C(q) = 109q + 93

# The revenue function for the same item is:

# R(q) = 109q + 48q / ln(q)

from sympy import *

init_printing()

def disp_fun( f ):
	pprint( '\n{0}\n\n'.format( pretty( f ) ) )

q = symbols( 'q' )

C = 109*q + 93
R = 109*q + ( 48*q / ln( q ) )

# Find the marginal cost.
m_cost = diff( C, q )

# Find the profit function.

P = R - C

disp_fun( P )

# The profit from one more unit when 8 units are sold is approximately
# ​(Type an integer or decimal rounded to two decimal places as​ needed.)

profit = diff( P, q ).subs( { q: 8 } ).evalf()
round( profit, 2 )