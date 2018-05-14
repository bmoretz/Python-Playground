from sympy import symbols, lambdify, solve
import matplotlib.pyplot as plt
import numpy as np

# Let ​g(x)
x = symbols( 'x' )
G = ( x + 3 ) / ( x**2 -2*x - 15 )

d = x**2 -2*x - 15
solve( d, x )

g_xlim = [ -30, 30 ]

lam_g = lambdify( x, G, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_g( x_vals )
plt.plot( x_vals, y_vals )
plt.show()


d = x**2 + 2*x - 8
solve( d, x )