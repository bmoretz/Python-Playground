from pulp import *

# A​ company's lawn seed mixtures contain three types of​ seeds: 
# bluegrass,​ rye, and Bermuda. 
# 
# The costs per pound of the three types are 
# 
#	9 ​cents, 
#	11 ​cents, and 
#	3​cents, respectively. 
#	
#	In each batch there must be 
#		at least 25​% bluegrass seed and 
#		the amount of Bermuda must be no more than ​two-thirds the amount of rye.

#	To fill current orders the company must make at least 6000 pounds of the mixture. 
#	
#	How much of each kind of seed should be used to minimize​ cost?

model = LpProblem( "Toy Production Problem", LpMinimize )

x1 = LpVariable( "x1", 0 ) # Classical
x2 = LpVariable( "x2", 0 ) # Jazz
x3 = LpVariable( "x3", 0 ) # Rock

model += x1 + x2 + x3

# Constraints

model += x1 + x2 <= 11
model += x3 <= 7
model += 2*x3 > x1

model.solve()
model.status

for variable in model.variables():
    print("{0} = {1}".format( variable.name, variable.varValue ) )

print( 'Optimal Sln: {0}'.format( pulp.value( model.objective ) ) )
