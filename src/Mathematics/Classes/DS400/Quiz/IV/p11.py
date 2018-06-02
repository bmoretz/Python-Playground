# Suppose that 9​% of a certain batch of calculators have a defective​ case, and that 12​% have defective batteries.​
#  Also, 4​% have both a defective case and defective batteries. A calculator is selected from the batch at random. 
#  
#  Find the probability that the calculator has a good case and good batteries.

pBC = .09
pGC = 1 - pBC

pBB = .12
bGB = 1 - pBB

pBCBB = 0.04

# Probabibility of bad case and bad batterise
pBC_BB = pBC + pBB - pBCBB

1 - pBC_BB