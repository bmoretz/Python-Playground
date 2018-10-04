from sympy import symbols, integrate, Rational, lambdify
import matplotlib.pyplot as plt
import numpy as np

# A small company of science writers found that its rate of profit​ (in thousands of​ dollars) after t years of operation is given by the function below.
t = symbols( 't' )
dP = ( 8*t + 8 ) * ( t**2 + 2*t + 2 ) ** Rational( 1, 3 )

P = integrate( dP, t )

# Find the total profit in the first three years. ( in thousands )
profit = integrate( dP, [ t, 0, 3 ] ).evalf()
round( profit * 1000 )

# The profit in the fourth year of operation is: (in thousands)
profit = integrate( dP, [ t, 3, 4 ] ).evalf()
round( profit * 1000 )

# How is the profit of company growing?
g_xlim = [ 1, 100 ]
g_ylim = [ -5, 15 ]

lam_p = lambdify( t, P, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_p( x_vals )
plt.plot( x_vals, y_vals )
plt.show()