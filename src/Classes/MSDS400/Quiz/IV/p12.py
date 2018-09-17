# Among uses of automated teller machines​ (ATMs), 
# 94​% use ATMs to withdraw cash and 31​% use them to check their account balance.

# Suppose that 96​% use ATMs to either withdraw cash or check their account balance​ (or both). 
# 
# Given a woman who uses an ATM to check her account​ balance, what the probability that she also uses an ATM to get​ cash? 

# P( C )
pC = .94

# P( B )
pB = .31

# P( C or B )
pBC = .96

# P( C and B ) = P( C ) + P( B ) - P( C OR B )
pB_C = pC + pB - pBC

# P( C/B ) = P( C and B) / P( B )
round( pB_C / pB, 3 )