import math
from sympy import Derivative, symbols, sin

# 6.2.1

x, y = symbols( 'x,y' )
Fx = 2*x + 2*y + x / y**2

dY = Derivative( Fx - 5, y ).doit()


dY