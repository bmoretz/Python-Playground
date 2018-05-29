
# An insurance company has written 
# 50 policies for ​$90,000​, 
# 100 policies for ​$40,000​, and 
# 250 policies for ​$10,000 for people of age 20. 
# 
# If experience shows that the probability that a person will die at age 20 is 0.0014​, 
# how much can the company expect to pay out during the year the policies were​ written?

prob = 0.0014
a = 50 * 90000 * prob
b = 100 * 40000 * prob
c = 250 * 10000 * prob

round( a + b + c )
