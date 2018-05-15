from sympy import *

# A psychologist contends that the number of facts of a certain type that are remembered after t hours is given by the following function.

t = symbols( 't' )
F = 88*t / ( 99*t - 88 )
dF = diff( F, t )

# Find the rate of change at which the number of facts remembered is changing after 1 hour and after 10 hours.

# The rate of change after 1 hour is about
one_hr = dF.subs( { t: 1 } )
# (Round to the nearest integer as​ needed)
round( one_hr )

# The rate of change after 10 hours is about
ten_hr = dF.subs( { t: 10 } ).evalf()
# (Round to the nearest integer as​ needed)
round( ten_hr )