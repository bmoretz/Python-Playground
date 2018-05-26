# A​ used-car dealer gets complaints about his cars as shown in the table.

complains = [ 0, 1, 2, 3, 4, 5, 6 ]
prob = [ 0.01, 0.04, 0.14, 0.24, 0.37, 0.1, 0.1 ]

ev = 0
for i in range( 0, len( complains ) ):
	ev += complains[ i ] * prob[ i ]

ev