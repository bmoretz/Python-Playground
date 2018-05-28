# Among uses of automated teller machines​ (ATMs), 
# 93​% use ATMs to withdraw cash and 31​% use them to check their account balance.
# Suppose that 97​% use ATMs to either withdraw cash or check their account balance​ (or both). 
# 
# Given a woman who uses an ATM to check her account​ balance, 
# what the probability that she also uses an ATM to get​ cash?

# P(C) = 0.93
pC = .93

# P( B) =0.31
pB = .31

# P( C or B )
pBC = .97

# P( C and B ) = P(C) +P (B) - P( C OR B ) = 0.93+0.31 - 0.97 = 0.27
pB_C = pC + pB - pBC

# P( C/B ) = P( C and B) / P( B )
round( pB_C / pB, 3 )