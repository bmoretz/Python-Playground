from sympy import symbols, solve
from fractions import Fraction

x1 = -2
y1 = 2

x2 = 2
y2 = 3

m = ( y1 - y2 ) / ( x1 - x2 ) 
Fraction( m ).limit_denominator()