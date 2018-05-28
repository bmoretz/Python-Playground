# A School of Public Health completed a study on alcohol consumption on college campuses. 
# They concluded that:
# 
# 21.5​% of women attending​ all-women colleges abstained from​ alcohol, compared to 
# 18.8​% of women attending coeducational colleges. Approximately 
# 5.6​% of women college students attend​ all-women schools. 
# 
# Complete parts​ (a) and​ (b) below.

# given women attending all women colleges, probabilty of abstained from alcohol P(Ab|AW)
pAb_AW = .215
# given women attending coed colleges, probabilty of abstained from alcohol P(Ab|CE)
pAb_CE = .188

# women attending all women college P(AW)
pAW = .056
# women attending coed P(CE)
pCE = 1 - pWA

# a
# What is the probability that a randomly selected female student abstains from​ alcohol?

# pAB =  P(Ab|AW) * P(AW) + P(Ab|CE) * P(CE)
pAb = round( pAb_AW * pAW + pAb_CE * pCE, 4 )


# b
# If a randomly selected female student abstains from​ alcohol, what is the probability she attends a coeducational​ college?

# P(Ab|CE) * P(CE) / P(Ab)

pCE_Ab = round( pAb_CE * pCE / pAb, 4 )