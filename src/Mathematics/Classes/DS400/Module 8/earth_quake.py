# There are seven geologic faults​ (and possibly​ more) capable of generating a magnitude 6.7 earthquake in the region around a certain city. 
# Their probabilities of rupturing by the year 2032 are 26​%, 18​%, 11​%, 10​%, 4​%, 3​%, and 3​%. Complete parts​ (a) and​ (b).

none = { 1, 1, 1, 1, 1, 1, 1 }
prob = { .26, .18, .11, .10, .04, .03, .03 }

prob = none | prob

round( prob, 4 )