# A bicycle factory runs two assembly​ lines, 
# A and B. 97​% of line​ A's products pass inspection and 90​% of line​ B's products pass inspection. 
# 40​% of the​ factory's bikes come off assembly line B and the rest come off line 
# 
# A. Find the probability that one of the​ factory's bikes passed inspection and came off assembly line B.

pP_A = .97
pP_B = .94

pF_A = round( 1 - pP_A, 2 )
pF_B = round( 1 - pP_B, 2 )

# 30% of the​ factory's bikes come off assembly line B and the rest come off line A
B = .3
A = 1 - A

#  Find the probability that one of the​ factory's bikes did not pass inspection and came off assembly line B.
pF_B * B