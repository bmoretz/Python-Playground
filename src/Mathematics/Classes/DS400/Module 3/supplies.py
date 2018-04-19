# A manufacturer purchases a part for use at both of its plants-one at​ Roseville, California, the other at​ Akron, Ohio. 
# The part is available in limited quantities from two suppliers.

# Each supplier has 80 units available. 

# The Roseville plant needs 20 ​units, and the Akron plant requires 80 units. 

# The first supplier charges ​$40 per unit delivered to Roseville and ​$70 per unit delivered to Akron. 

# Corresponding costs from the second supplier are ​$50 and ​$100. 

# The manufacturer wants to order a total of 80 units from the​ first, less expensive​ supplier, with the remaining 20 units to come from the second supplier. 
# If the company spends ​$7000 to purchase the required number of units for the two​ plants, find the number of units that should be sent from each supplier to each plant.

# Write a linear system of equations. 

# The number of units sent from the first supplier to Roseville is​ w, 
# the number of units sent from the first supplier to Akron is​ x, 
# the number of units sent from the second supplier to Roseville is​ y, 
# and the number of units sent from the second supplier to Akron is z. 

# Choose the correct answer below.

from sympy import symbols, solve

w,x,y,z = symbols( 'w,x,y,z' )

# w + y = 20
expr1 = w + y - 20
# w + x = 80
expr2 = w + x - 80
# w + x + y + z = 100
expr3 = w + x + y + z - 100
# 40*w + 70*x + 50*y + 100*z
expr4 = 40*w + 70*x + 50*y + 100*z - 7000

solve( ( expr1, expr2, expr3, expr4 ), dict = True )