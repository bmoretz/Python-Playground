# A study showed that 69.6​% of occupants involved in a fatal car crash wore seat belts. 
# Of those in a fatal car crash who wore seat​ belts, 4​% were ejected from the vehicle. 
# 
# For those not wearing seat​ belts, 36​% were ejected from the vehicle.

# S = seat belt, J = ejected

pS = .696
pNS = 1 - pS

pJS = .36
pJNS = .04

# Find the probability that a randomly selected person in a fatal car crash who was ejected from the vehicle was wearing a seatbelt.
bayes = ( pS * pJNS ) / ( pS * pJNS + pNS * pJS )
round( bayes, 4 )

# Find the probability that a randomly selected person in a fatal car crash who was not ejected from the vehicle was not wearing a seatbelt.
bayes = ( pNS * ( 1 - pJS ) ) / ( pS * ( 1 - pJNS ) + pNS * ( 1 - pJS ) )
round( bayes, 4 )