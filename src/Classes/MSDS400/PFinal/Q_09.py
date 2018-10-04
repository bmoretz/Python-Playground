from sympy import ( symbols, lambdify, diff, exp, solve, pprint )
import matplotlib.pyplot as plt
import numpy as np

g_xlim = [ -5, 40 ]
g_ylim = [ -5, 70 ]

def plot_fun( fun, name, col ):
	x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
	y_vals = fun( x_vals )
	plt.plot( x_vals, y_vals, label = name, color = col )

# The equation:

initial_investment = 4000
compounding_rate = 3.5 / 100

# gives the balance after t years of an initial investment of $ dollars which pays ​% compounded continuously.  

t = symbols( 't' )
A = initial_investment * exp( compounding_rate * t )

dA_dt = diff( A, t )
pprint( dA_dt )

# A'( 6 ) = 
fv_12 = dA_dt.subs( { t: 6 } )
round( fv_12 )

lam_g = lambdify( t, A, np )
plot_fun( lam_g, 'A', 'G' )

lam_dg = lambdify( t, dA_dt, np )
plot_fun( lam_dg, 'dA/dt', 'B' )

delta = A.subs( { t: 7 } ) - A.subs( { t: 6 } )
round( delta, 2 )

plt.legend()
plt.show()