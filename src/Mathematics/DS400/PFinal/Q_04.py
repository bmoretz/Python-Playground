from pulp import *

# A​ company's lawn seed mixtures contain three types of​ seeds: 
# bluegrass,​ rye, and Bermuda. 
# 
# The costs per pound of the three types are 
# 
#	11 ​cents, 
#	14 ​cents, and 
#	6 ​cents, respectively. 
#	
#	In each batch there must be 
#		at least 25​% bluegrass seed and 
#		the amount of Bermuda must be no more than ​two-thirds the amount of rye.

#	To fill current orders the company must make at least 6000 pounds of the mixture. 
#	
#	How much of each kind of seed should be used to minimize​ cost?

model = LpProblem( "Toy Production Problem", LpMinimize )

x1 = LpVariable( "x1", 0 ) # Bluegrass
x2 = LpVariable( "x2", 0 ) # Rye
x3 = LpVariable( "x3", 0 ) # Bermuda

model += .11*x1 + .14*x2 + .06*x3

# Constraints

model += x1 >= .25 * ( x1 + x2 + x3 )
model += x3 <= 2/3*x2

model += x1 + x2 + x3 >= 6000

model.solve()
model.status

for variable in model.variables():
    print("{0} = {1}".format( variable.name, variable.varValue ) )

print( 'Optimal Sln: {0}'.format( pulp.value( model.objective ) ) )