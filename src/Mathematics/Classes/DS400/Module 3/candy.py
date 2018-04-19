# A candy company has 132 kg of​ chocolate-covered nuts and 90 kg of​ chocolate-covered raisins to be sold as two different mixes. 

# One mix will contain half nuts and half raisins and will sell for​ $7 per kg. 
# The other mix will contain three fourths nuts and one fourth raisins and will sell for​ $9.50 per kg.

# Complete parts a. and b.

# a. How many kilograms of each mix should the company prepare for the maximum​ revenue? 
# Find the maximum revenue.

# b. The company raises the price of the second mix to​ $11 per kg. Now how many kilograms of each mix should the company prepare for the maximum​ revenue? 
# Find the maximum revenue.

from pulp import *

candy = LpProblem( "Candy Problem", LpMaximize )

x = LpVariable( "x", 0 ) # Mix #1
y = LpVariable( "y", 0 ) # Mix #2

w = LpVariable( "w" )

candy += 7*x + 11*y

# Constraints

candy += .5*x + .75*y <= 132
candy += .5*y + .25*y <= 90

candy.solve()
candy.LpStatus[ candy.status ]

for variable in candy.variables():
    print("{0} = {1}".format( variable.name, variable.varValue ))

print( 'Optimal Sln: {0}'.format(pulp.value( candy.objective )))