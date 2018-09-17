from sympy import ( symbols, solve, diff, integrate, exp, sqrt, lambdify, Integral, pprint, oo )
import matplotlib.pyplot as plt
import numpy as np

x = symbols( 'x', real = True )

# Find the expected​ value, the​ variance, and the standard​ deviation, when they​ exist, for the probability density function.

f1 = ( x** 3 ) / 12
f2 = 128 / ( 3*x ** 5 )

a, b, c, d = 0, 2, 2, oo

# What is the expected​ value?
ev = ( integrate( f1 * x, ( x, a, b ) ) + integrate( f2 * x, ( x, c, d ) ) ).evalf()
round( ev, 2 )

# The variance is ​Var(X)
var = integrate( ( ( x **2 ) * f1 ), ( x, a, b ) ) +  integrate( ( ( x **2 ) * f2 ), ( x, c, d ) ) - ev**2
round( var, 2 )

# The standard deviation is
stdev = sqrt( var )
round( stdev, 2 )