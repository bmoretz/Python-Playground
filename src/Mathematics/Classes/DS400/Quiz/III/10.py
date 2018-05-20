from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# here is a mathematical relationship between an​ infant's weight and total body surface area​ (BSA), given by

w = symbols( 'w' )
A = 4.688 * w ** ( 0.8168 - 0.0154*log( w, 10 ) )

# where w is the weight​ (in grams) and​ A(w) is the BSA in square centimeters.

# Find the BSA for an infant who weighs.
weight = 4143

bsa = A.subs( { w: weight } ).evalf()
# ​(Round to the nearest integer as​ needed.)
round( bsa )

# Find Upper A' right parenthesis.
dA = Derivative( A, w ).doit()
bsap = dA.subs( { w: weight } ).evalf()
round( bsap, 2 )

# graph A(w) on [2000, 10,000] by​ [0, 6000]

g_xlim = [ 2000, 10000 ]
g_ylim = [ 0, 6000 ]

lam_a = lambdify( w, A, np )

x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_a( x_vals )
plt.plot( x_vals, y_vals )
plt.show()