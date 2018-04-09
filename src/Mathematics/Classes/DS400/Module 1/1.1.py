import math
from datetime import datetime, timedelta
from math import pi
from fractions import Fraction
from sympy import symbols

# What is the volume of a sphere with radius r is 4/3 pi r^3. What is the volume of a sphere with radius 5?

def sphere_vol( r ):
	return Fraction( 4, 3 ) * pi * r ** 3

# 1

round( sphere_vol( 5 ), 1 )

# 2

c, x = symbols( 'c, x' )
Fx = ( .6 * x * c ) + ( 3 + .75*(x - 1) )
sln = Fx.subs( { c: 24.95, x: 60 } ).evalf()
round( sln, 2 )

# 3
n = datetime.today()
n = n.replace( hour = 6, minute = 52 ) 

r = 2 * timedelta( minutes = 8, seconds = 15 ) + 3 * timedelta( minutes = 7, seconds = 12 )

str( n + r )