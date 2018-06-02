# On a​ ballot, the candidates for each office are listed together under the office for which they are running. 
# In an election with 3 candidates for one office and 5 candidates for another​ office, 
# how many different versions of the ballot are​ possible?

import math

# There are 6 candidates for one office
# Therefore ther are 6! ways for ballot

# There are 3 candidates for another office
# Therefore therare 3! ways for ballot

# And also there are 2 offices, 
# therefore there are 2! ways ballot

math.factorial( 6 ) * math.factorial( 3 ) * math.factorial( 2 )