# A farmer has 600 acres of available land and ​$120,000 to spend. 
# He wants to plant the combination of crops which maximizes his profit. 
# Complete parts​ (a) through​ (c).
# 

from pulp import *

num_acres = 480
cost_per_acre = 72000

pot_cost = 320
pot_profit = 120

cab_cost = 224
cab_profit = 60

corn_cost = 128
corn_profit = 40

farm_prob = LpProblem( "Land Area", LpMinimize )

y1 = LpVariable( "y1", 0 )
y2 = LpVariable( "y2", 0 )
w = LpVariable( "w" )

farm_prob += num_acres*y1 + cost_per_acre*y2, "Objective"

# Constraints

farm_prob += y1 + pot_cost*y2 >= pot_profit
farm_prob += y1 + cab_cost*y2 >= cab_profit
farm_prob += y1 + corn_cost*y2 >= corn_profit

farm_prob.solve()
pulp.LpStatus[farm_prob.status]

for variable in farm_prob.variables():
    print("{0} = {1}".format(variable.name, variable.varValue))

print( 'Optimal Sln: {0}'.format(pulp.value(farm_prob.objective)))

# shadow
# 0 * 400 + .375 * 88000

.375 * 72000