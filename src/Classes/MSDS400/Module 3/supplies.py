# A manufacturer purchases a part for use at both of its plantsdashone at​ Roseville, California, the other at​ Akron, Ohio. 
# The part is available in limited quantities from two suppliers. 

# Each supplier has 85 units available. 

# The Roseville plant needs 50 ​units, and the Akron plant requires 85 units. 

# The first supplier charges ​$50 per unit delivered to Roseville and ​$80 per unit delivered to Akron. 

# Corresponding costs from the second supplier are ​$90 and ​$110. 

# The manufacturer wants to order a total of 85 units from the​ first, less expensive​ supplier, with the remaining 50 units to come from the second supplier. 
# If the company spends ​$10,800 to purchase the required number of units for the two​ plants, find the number of units that should be sent from each supplier to each plant.

# Write a linear system of equations. 

# The number of units sent from the first supplier to Roseville is​ w, 
# the number of units sent from the first supplier to Akron is​ x, 
# the number of units sent from the second supplier to Roseville is​ y, 
# and the number of units sent from the second supplier to Akron is z. 

# Choose the correct answer below.

from sympy import symbols, solve

w,x,y,z = symbols( 'w,x,y,z' )

# w + y = 50
expr1 = w + y - 50

# w + x = 85
expr2 = w + x - 85

# w + x + y + z = 135
expr3 = w + x + y + z - 135

# 50*w + 80*x + 90*y + 110*z
expr4 = 50*w + 80*x + 90*y + 110*z - 10800

solve( ( expr1, expr2, expr3, expr4 ), dict = True )
