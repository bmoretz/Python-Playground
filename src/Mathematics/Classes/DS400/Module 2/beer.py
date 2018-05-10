# Customers buy 15 units of regular beer and 16 units of light beer monthly. 
# The brewery decides to produce extra​ beer, beyond that needed to satisfy the customers. 
# The cost per unit of regular beer is ​$31,000 and the cost per unit of light beer is ​$44,000. 
# Every unit of regular beer brings in ​$300,000 in​ revenue, while every unit of light beer brings in ​$600,000 in revenue. 
# The brewery wants at least ​$30,000,000 in revenue. 
# At least 37 additional units of beer can be sold. Complete parts​ (a) and​ (b).
#

from pulp import *

reg_beer_cost = 34000
lt_beer_cost = 45000

reg_rev = 150000
lg_rev = 300000

min_rev = 9300000

total_units = 14 + 19 + 11

print( 'total units at least: {0}'.format( total_units ) )

prob_a = LpProblem( "Beer Production", LpMinimize )

y1 = LpVariable( "y1", 0 )
y2 = LpVariable( "y2", 0 )
w = LpVariable( "w" )

prob_a += reg_beer_cost*y1 + lt_beer_cost*y2, "Objective"

# Constraints

prob_a += y1 + y2 >= total_units
prob_a += reg_rev * y1 + lg_rev * y2 >= min_rev

prob_a.solve()
pulp.LpStatus[prob_a.status]

for variable in prob_a.variables():
    print("{0} = {1}".format(variable.name, variable.varValue))

print( 'Optimal Sln: {0}'.format(pulp.value(prob_a.objective)))

prob_b = LpProblem( "Beer Production", LpMaximize )

x1 = LpVariable( "x1", 0 )
x2 = LpVariable( "x2", 0 )
z = LpVariable( "z" )

prob_b += total_units*x1 + min_rev*x2, "Objective"

# Constraints

prob_b += x1 + reg_rev*x2 == reg_beer_cost
prob_b += x1 + lg_rev*x2 == lt_beer_cost
prob_b += -total_units*x1 - min_rev*x2 + z == 0

prob_b.solve()
pulp.LpStatus[prob_b.status]

for variable in prob_b.variables():
    print("{0} = {1}".format(variable.name, variable.varValue))

print( 'Optimal Sln: {0}'.format(pulp.value(prob_b.objective)))