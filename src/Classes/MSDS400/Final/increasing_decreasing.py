# The number of people P(t) (in hundreds) infected t days after an epidemic begins is
# approximated by the function below. When will the number of people infected start to decline?

from sympy import ( solve, diff, symbols, ln, pprint, init_printing, simplify, lambdify )
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

g_xlim = [ 1, 15 ]

init_printing()

def plot_fun( fun, name ):
	x_vals = np.linspace( g_xlim[0], g_xlim[1], 100, endpoint=True )
	y_vals = fun( x_vals )
	plt.plot( x_vals, y_vals, label = name )

t = symbols( 't' )
Pt = 10 * ln( 0.19*t + 1 ) / ( 0.19*t + 1 )

pprint( Pt )

dP_dt = simplify( diff( Pt, t ) )
pprint( dP_dt )

critical_point = solve( dP_dt )[ 0 ]

fp = lambdify( t, Pt, np )
plot_fun( fp, 'Infected' )

plt.scatter( x = critical_point, y = Pt.subs( { t: critical_point } ), color = 'Black', label = 'Decreasing' )

plt.title( 'Epidemic in days' )
plt.legend()
plt.show()