# A study on optimizing revenue from a website considered dividing customers into two groups based on a value x between 0 and​ 1, 
# where x measures the proportion of the total bandwidth requested by a customer. 
# Customers with a request less than x were considered low​ revenue, and those above x high revenue. 
# The expected revenue from the low revenue customers was described by the following​ function, 
# where C and k are positive constants based on attributes of the website and the customers.

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

domain_end = 20

g_xlim = [0, 40]
g_ylim = [0, 70]

# eq

x = sp.Symbol( 'x' )
C, k = sp.symbols( 'C k', positive = True )
R = C * k * ( 1 - np.e**( -k*x ) )
dR = diff( R, x )

lam_x = sp.lambdify( x, R, modules=[ "numpy", "sympy" ] )

x_vals = range = np.arange( 0.001, 1, 1/20.)
y_vals = lam_x( x_vals )

