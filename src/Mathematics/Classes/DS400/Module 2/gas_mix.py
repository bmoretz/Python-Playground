# A company is developing a new additive for gasoline. 
# The additive is a mixture of three liquid​ ingredients, I,​ II, and III. 
# For proper​ performance, the total amount of additive must be at least 7 oz per gal of gasoline.​ 
# However, for safety​ reasons, the amount of additive should not exceed 19 oz per gal of gasoline. 
# At least one sixth oz of ingredient I must be used for every ounce of ingredient​ II, and at least 1 oz of ingredient III must be used for every ounce of ingredient I. 
# The costs of​ I, II, and III are ​$0.40​, ​$0.24​, and ​$0.64 per​ oz, respectively.

from pulp import *

gax_mix = LpProblem( "Gas Mixture Problem", LpMinimize )

y1 = LpVariable( "y1", 0 )
y2 = LpVariable( "y2", 0 )
y3 = LpVariable( "y3", 0 )

w = LpVariable( "w" )

gax_mix +=  .40*y1 + .16*y2 + .64*y3

# Constraints

gax_mix += y1 + y2 + y3 >= 10
gax_mix += y1 + y2 + y3 <= 16

gax_mix += 6*y1 >= y2
gax_mix += y1 <= y3

gax_mix.solve()
gax_mix.LpStatus[gax_mix.status]

for variable in gax_mix.variables():
    print("{0} = {1}".format(variable.name, variable.varValue))

print( 'Optimal Sln: {0}'.format(pulp.value(gax_mix.objective)))