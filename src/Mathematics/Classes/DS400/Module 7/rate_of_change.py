from sympy import solve, symbols, lambdify, diff, Integral, exp, pprint, pretty, simplify
import matplotlib.pyplot as plt
import numpy as np

t = symbols( 't', positive = True )
# The approximate rate of change in the number​ (in billions) of monthly text messages is given by the equation
F = 8.1*t - 16.3
# where t represents the number of years since 2000

#  In 2005 ​(t=5​) there were approximately 9.6 billion monthly text messages
year, value = 5, 9.6

# Find the function that gives the total number​ (in billions) of monthly text messages in year t
F = Integral( F, t ).doit()

C = F.subs( { t: year } ) - value

fun = F - C

# According to this​ function, how many monthly text messages were there in​ 2009 ( 2009 - 2000 )
y = 2009 - 2000
round( fun.subs( { t: y } ), 2 )