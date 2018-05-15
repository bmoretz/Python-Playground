from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# The average monthly rent for a​ 1000-sq-ft apartment in a major metropolitan area from 
# 1998 through 2005 can be approximated by the function below where t is the time in years since 
# the beginning of 1998. Find the value of t when rents were increasing most rapidly. 
# Approximately when did this​ occur?

t = symbols( 't', positive = True ) # 0 <= x
C = 1.6668 * t**4 - 16.746 * t**3 + 62.39 * t**2 + 6.9317 * t + 1005

# The rents were increasing most rapidly when 
dC = diff( C, t, 1 )
ddC = diff( C, t, 2 )

critical_points = solve( ddC, t )

c1 = C.subs( { t: critical_points[ 0 ] } )
c2 = C.subs( { t: critical_points[ 1 ] } )

# c2 is higher, so
# The rents were increasing most rapidly when
round( critical_points[ 1 ], 3 )

# Then round to three decimal places as​ needed.)
year = round( 1998 + critical_points[ 1 ] )
year