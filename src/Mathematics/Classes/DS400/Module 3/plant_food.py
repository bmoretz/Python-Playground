# A plant food is made from three​ chemicals, labeled​ I, II, and III. 

# In each batch of the plant​ food, 
# the amounts of chemicals II and III must be in the ratio of 5 to 2. 
# The amount of nitrogen must be at least 75 kg. 
# The percent of nitrogen in the three chemicals is 9​%, 6​%, and 3​%, respectively. 

# If the three chemicals cost ​$1.07​, ​$0.84​, and ​$0.67 per​ kilogram, respectively,
# how much of each should be used to minimize the cost of producing at least 900 kg of the plant​ food?

from pulp import *

plant_food = LpProblem( "Algea Problem", LpMinimize )

x1 = LpVariable( "x1", 0 ) # Chem I
x2 = LpVariable( "x2", 0 ) # Chem II
x3 = LpVariable( "x3", 0 ) # Chem III

w = LpVariable( "w" )

plant_food += 1.07*x1 + .84*x2 + .67*x3

# Constraints

plant_food += 2*x2 == 5*x3 # 2 to 5.
plant_food += .09*x1 + .06*x2 + .03*x3 >= 75
plant_food += x1 + x2 + x3 >= 900

plant_food.solve()
plant_food.LpStatus[ plant_food.status ]

for variable in plant_food.variables():
    print("{0} = {1}".format( variable.name, variable.varValue ))

print( 'Optimal Sln: {0}'.format( pulp.value( plant_food.objective )))