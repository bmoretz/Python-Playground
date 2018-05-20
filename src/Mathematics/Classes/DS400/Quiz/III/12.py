from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# Suppose that the cost function for a product is given by
x = symbols('x', positive = True ) # 0 <= x
C = 0.002 * x**3 + 7*x + 7626

avgC = C / x

g_xlim = [ 1, 500 ]

lam_c = lambdify( x, avgC, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 10000, endpoint=True )
y_vals = lam_c( x_vals )

plt.plot( x_vals, y_vals, label = '' )

daC = diff( avgC, x, 1 )

# The production level that produces the minimum average cost per unit is
min = solve( daC, x )[ 0 ]
min

# ​(Round to the nearest whole number as​ needed.)
round( min )

plt.show()