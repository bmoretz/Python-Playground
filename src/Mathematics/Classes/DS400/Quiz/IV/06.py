from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, pprint )
import matplotlib.pyplot as plt
import numpy as np

# The difference between the true value of an integral and the value given by the trapezoidal rule or​ Simpson's rule is known as the error. 
# In numerical​ analysis, the error is studied to determine how large n must be for the error to be smaller than some specified amount. 
# 
# For both​ rules, the error is inversely proportional to a power of​ n, the number of subdivisions.

# In other​ words, the error is roughly StartFraction k / n^p 
# where k is a constant that depends on the function and the​ interval, and p is a power that depends only on the method used. 
# With a little​ experimentation, you can find out what the power p is for the trapezoidal rule and for​ Simpson's rule.

def simpsons_rule( f, a, b, n ):
	area = 0

	steps = np.linspace( a, b, n + 1, endpoint = True )

	for i in range( 0, n + 1 ):

		v = f.subs( { x: steps[ i ] } )

		if i == 0 or i == n:
			area += v
		elif i % 2 == 0:
			area += 2 * v
		else:
			area += 4 * v

	return area * ( b - a ) / ( 3*n )

# Function

x = symbols( 'x' )
F = 11*x**4

# What does the petal distribution look like?

g_xlim = [ -.01, 2 ]

lam_p = lambdify( x, F, np )
x_vals = np.linspace( g_xlim[0], g_xlim[1], 1000, endpoint=True )
y_vals = lam_p( x_vals )
plt.plot( x_vals, y_vals )

x_min, x_max = 0, 1

plt.vlines( x = x_min, ymin = 0, ymax = F.subs( { x: x_min } ), color = 'Black', zorder = 1 )
plt.vlines( x = x_max, ymin = 0, ymax = F.subs( { x: x_max } ), color = 'Red', zorder = 1 )

plt.show()

#  Find the exact value of
a, b = 0, 1
area = integrate( F, ( x, a, b ) ).evalf()

# Approximate the integral in part a using​ Simpson's rule with n = ​4, ​8, 16, and 32
n = 4
n4 = round( simpsons_rule( F, a, b, n ), 7 )
n4
e4 = round( abs( area - n4 ), 7 )
'{:.7f}'.format( abs( n4 - area ) )

n = 8
n8 = round( simpsons_rule( F, a, b, n ), 7 )
n8
e8 = abs( area - n8 )
'{:.7f}'.format( abs( n8 - area ) )

n = 16
n16 = round( simpsons_rule( F, a, b, n ), 7 )
n16
e16 = abs( n16 - area )
'{:.7f}'.format( e16 )

n = 32
n32 = round( simpsons_rule( F, a, b, n ), 7 )
n32
e32 =  abs( n32 - area )
'{:.7f}'.format( e32 )

# c
#  If the error is k/n**p, then the error times n Superscript p should be approximately a constant. Multiply the errors in part b times n**p for p=1, ​2, etc., 
#  until you find a power p yielding approximately the same answer for all four values of n.

p = 4

e4 * 4 ** p
e8 * 8 ** p
e16 * 16 ** p
e32 * 32 ** p