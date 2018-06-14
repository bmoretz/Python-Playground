import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from math import factorial as fac

g_xlim = [ 1, 7 ]

def plot_fun( fun, name ):
	x_vals = np.linspace( g_xlim[0], g_xlim[1], 100, endpoint=True )
	y_vals = fun( x_vals )
	plt.plot( x_vals, y_vals, label = name )

def factorial(n):
    return functools.reduce((lambda x,y: x*y),range(1,n+1))

def N( x ):
	return x

def C( x ):
	return 1

def log( x ):
	return np.log( x )

def log_4( x ):
	return np.log( x ** 4 )

def nlogn( x ):
	return x * np.log( x )

def nsq( x ):
	return x**2

def npower( x ):
	return 2**x

def nfac( x ):
	return fac( x )

plot_fun( log, "log" )
plot_fun( N, "N" )
plot_fun( nlogn, "n log n" )
plot_fun( nsq, "n²" )
plot_fun( npower, "2ⁿ" )
plot_fun( log_4, "log^4" )

plt.legend()
plt.show()