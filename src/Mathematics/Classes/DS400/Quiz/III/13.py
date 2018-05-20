from sympy import *

# The average monthly rent for a​ 1000-sq-ft apartment in a major metropolitan area from 
# 1998 through 2005 can be approximated by the function below where t is the time in years since 
# the beginning of 1998. Find the value of t when rents were increasing most rapidly. 
# Approximately when did this​ occur?

t = symbols( 't', positive = True ) # 0 <= x
C = 1.6434 * t**4 - 21.052 * t**3 + 62.98 * t**2 + 6.1157 * t + 1005

# The rents were increasing most rapidly when 
dC = diff( C, t, 1 )
ddC = diff( dC, t, 1 )

critical_values = solve( ddC )

cv_1 = dC.subs( { t : critical_values[ 0 ] } )
cv_2 = dC.subs( { t : critical_values[ 1 ] } )

if cv_1 > cv_2:
	cv = critical_values[ 0 ]
	print( 'Critical Value {0} is higher [ {1} ]'.format( round( cv, 3 ), cv_1 ) )
else:
	cv = critical_values[ 1 ]
	print( 'Critical Value {0} is higher [ {1} ]'.format( round( cv, 3 ), cv_2 ) )

print( 'Year: {0}'.format( round( 1998 + cv ) ) )