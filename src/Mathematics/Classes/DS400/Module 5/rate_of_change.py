# Suppose the demand for a certain item is given by ​D(p) -5p^2 7p +600​, where p represents the price of the item in dollars.

# a. Find the rate of change of demand with respect to price.
# b. Find and interpret the rate of change of demand when the price is ​$10.

from sympy import symbols, Limit, Derivative, Integral

p = symbols( 'p' )
fP = -5*p**2 - 7*p + 600

dP = Derivative( fP, p ).doit()

# The rate of change of demand with respect to price is
dP


# When the price is ​$10​, demand is: 
dP.subs( { p: 10 } )
# decreasing at a rate of about  107 items for each increase in price of​ $1.
