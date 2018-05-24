# A manufacturing firm finds that 60​% of its new hires turn out to be good workers and 40 % become poor workers. 
# All current workers are given a reasoning test. 
# 
# Of the good​ workers, 90​% pass​ it; 30​% of the poor workers pass it. 
# Assume that these figures will hold true in the future. 
# 
# If the company makes the test part of its hiring procedure and only hires people who meet the previous requirements and also pass the test, what percent of the new hires will turn out to be good​ workers?

workers = 1
good = .6
bad = workers - good

good_passed = .9
bad_passed = .3

prob = ( good * good_passed ) / ( good * good_passed + bad * bad_passed )

round( prob, 1 ) * 100
