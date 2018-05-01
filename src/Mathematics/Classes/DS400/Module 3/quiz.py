from sympy import symbols, solve
from math import *
# 2x2 + x3logx is O(x^n)

x,n = symbols( 'x, n' )
fx = 2*x**2 + 3*x*log10(x) == 