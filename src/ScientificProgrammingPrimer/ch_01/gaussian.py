import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mu = 0
sigma = 2

def f(x):
	return 1/ ( np.sqrt( 2*np.pi ) * sigma ) * np.exp( -.5 * ( ( x - mu ) / sigma ) **2 )

x = np.arange( -4.0, 4.0, 0.1 )

plt.plot( x, f(x) )
plt.show()