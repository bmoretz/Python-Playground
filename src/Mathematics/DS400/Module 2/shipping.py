# An oil company supplies two distributors in the northwest from two​ outlets, S1 and S2. 
# Distributor D1 needs at least 3000 barrels of​ oil, and distributor Upper D 2 needs at least 5000 barrels. 
# The two outlets can each furnish up to 5000 barrels of oil. 
# The costs per barrel to ship the oil are given in the accompanying table. 
# There is also a shipping tax per barrel as given in the accompanying table. 
# The oil company is determined to spend no more than ​$40 comma 000 on shipping tax. Complete parts​ (a) and​ (b) below.
	
# 					
# Costs per Barrel to Ship Oil
#		D1	 D2
#	S1	​$30	​$22
#	S2	​$25	​$20

# 	Tax per Barrel
#		D1	D2
#	S1	​$22	​$66
#	S2	​$55	​$4


from pulp import *

d1_barrels = 3000
d2_barrels = 5000

d1_s1_cost = 30
d2_s1_cost = 22
d1_s2_cost = 25
d2_s2_cost = 20

d1_s1_tax = 2
d2_s1_tax = 6
d1_s2_tax = 5
d2_s2_tax = 4

shipping_cost = LpProblem( "Shipping Cost Problem", LpMinimize )

y1 = LpVariable( "y1", 0 )
y2 = LpVariable( "y2", 0 )
y3 = LpVariable( "y3", 0 )
y4 = LpVariable( "y4", 0 )

w = LpVariable( "w" )

shipping_cost += d1_s1_cost *y1 + d2_s1_cost * y2  + d1_s2_cost * y3 + d2_s2_cost * y4

# Constraints

shipping_cost += y1 + y3 >= d1_barrels
shipping_cost += y2 + y4 >= d2_barrels

shipping_cost += y1 + y2 <= 5000
shipping_cost += y3 + y4 <= 5000

# Tax

shipping_cost += d1_s1_tax*y1 + d2_s1_tax*y2  + d1_s2_tax*y3 + d2_s2_tax*y4 <= 40000

shipping_cost.solve()
pulp.LpStatus[shipping_cost.status]

for variable in shipping_cost.variables():
    print("{0} = {1}".format(variable.name, variable.varValue))

print( 'Optimal Sln: {0}'.format(pulp.value(shipping_cost.objective)))