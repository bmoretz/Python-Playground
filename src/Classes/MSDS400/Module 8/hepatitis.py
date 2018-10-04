# The probability that a person with certain symptoms has hepatitis is 0.75. 
# The blood test used to confirm this diagnosis gives positive results for 91​% of people with the disease and 5​% of those without the disease. 
# What is the probability that an individual who has the symptoms and who reacts positively to the test actually has​ hepatitis?

pF = .75
pNF = 1 - pF

pE = .91
pNE = 1 - pE

pH = .05

bayes = ( pF * pE ) / ( pF * pE + pNF * pH )

round( bayes, 4 )