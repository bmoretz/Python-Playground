# An electronics company produces​ transistors, resistors, and computer chips.

# Each transistor requires 3 units of​ copper, 2 units of​ zinc, and 1 unit of glass. 
# Each resistor requires 3​, 1​, and 2 units of the three​ materials, 
# and each computer chip requires 2​, 1​, and 2 units of these​ materials, respectively. 
# How many of each product can be made with the following amounts of​ materials? Complete parts​ (a) through​ (c) below.

# Let x represent the number of transistors that can be​ made, y the number of​ resistors, and z the number of computer chips. 
# Write a system of three linear equations when the amounts of available materials are 835 units of​ copper, 410 units of​ zinc, and 520 units of glass. 
# Choose the correct answer below.

from pulp import *

electronics = LpProblem( "Electronics Problem", LpMaximize )

x = LpVariable( "x", 0 ) # transistors
y = LpVariable( "y", 0 ) # resistors
z = LpVariable( "z", 0 ) # computer

w = LpVariable( "w" )

electronics += x + y + z

# Constraints

electronics += 3*x + 3*y + 2*z == 1035 # copper
electronics += 2*x + y + z == 525 # zinc
electronics += x + 2*y + 2*z == 600 # glass

electronics.solve()
electronics.LpStatus[electronics.status]

for variable in electronics.variables():
    print("{0} = {1}".format( variable.name, variable.varValue ))

print( 'Optimal Sln: {0}'.format(pulp.value( electronics.objective )))