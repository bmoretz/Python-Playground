import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

g_xlim = [ 1, 80 ]

def plot_fun( fun, name ):
	x_vals = np.linspace( g_xlim[0], g_xlim[1], 100, endpoint=True )
	y_vals = fun( x_vals )
	plt.plot( x_vals, y_vals, label = name )

def C( x ):
	return 12*x + 240

def R( x ):
	return 18*x

def P( x ):
	return R( x ) - C( x )

plot_fun( C, "C" )
plot_fun( R, "R" )
plot_fun( P, "P" )

plt.legend()
plt.show()

C(1) - R(1)