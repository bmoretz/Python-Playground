# A biologist must make a nutrient for her algae. 
# The nutrient must contain the three basic elements​ D, E, and​ F, 
# and must contain at least 
# 10 kg of​ D, 
# 18 kg of​ E, 
# and
# 20 kg of F. 

# The nutrient is made from three​ ingredients, I, II and III. 
# The quantity of​ D, E, and F in one unit of each of the ingredients is as given in the chart. 
# How many units of each ingredient are required to meet the​ biologist's needs at minimum​ cost?

from pulp import *

algea = LpProblem( "Algea Problem", LpMinimize )

y1 = LpVariable( "y1", 0 ) # Ingredient I
y2 = LpVariable( "y2", 0 ) # Ingredient II
y3 = LpVariable( "y3", 0 ) # Ingredient III

w = LpVariable( "w" )

algea += 3*y1 + 7*y2 + 4*y3

# Constraints

algea += 3*y1	+ 2*y2	+ 11*y3		>= 10 # D
algea += 6*y1	+ 4*y2	+ 2*y3		>= 18 # E
algea += 0*y1	+ 3*y2	+ 4*y3		>= 20 # F

algea.solve()
algea.status

for variable in algea.variables():
    print("{0} = {1}".format( variable.name, variable.varValue ))

print( 'Optimal Sln: {0}'.format(pulp.value( algea.objective )))