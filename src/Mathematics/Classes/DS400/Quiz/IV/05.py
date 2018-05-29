from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, pprint, Integral, simplify )
import matplotlib.pyplot as plt
import numpy as np

x = symbols( 'x' )

# A construction company has an expenditure rate of
dE = exp( 0.13*x )
E = integrate( dE, x )

#  dollars per day on a particular paving job and an income rate
dI = 116.3 - exp( 0.13 * x )
I = integrate( dI, x )

# dollars per day on the same​ job, where x is the number of days from the start of the job. 

# The​ company's profit on that job will equal total income less total expenditures. 
# 
# Profit will be maximized if the job ends at the optimum​ time, which is the point where the two curves meet.

P = I - E

# What is the graph doing?
g_xlim = [ 1, 40 ]

lam_e = lambdify( x, dE, np )
x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_e( x_vals )
plt.plot( x_vals, y_vals, label = "Expense" )

lam_i = lambdify( x, dI, np )
x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_i( x_vals )
plt.plot( x_vals, y_vals, label = "Income" )

days = solve( dI - dE, x )[ 0 ]

lam_p = lambdify( x, P, np )
x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_p( x_vals )
plt.plot( x_vals, y_vals, label = "Profit" )

plt.vlines( x = days, ymin = 0, ymax = P.subs( { x: days } ), color = 'Red', zorder = 1 )

income = round( I.subs( { x: days } ), 2 )
expenses = round( E.subs( { x: days } ), 2 )
max_profit = round( P.subs( { x: days } ), 2 )

plt.title( 'Max Profit at {0} days, ${1}'.format( days, max_profit ) )
plt.legend()
plt.show()

if __name__ == '__main__':
	print( 'Optimal Days: {0}'.format( round( days ) ) )
	print( 'Total Income: {0}'.format( income ) )
	print( 'Total Expenditures: {0}'.format( expenses ) )
	print( 'Max Profit: {0}'.format( max_profit ) )