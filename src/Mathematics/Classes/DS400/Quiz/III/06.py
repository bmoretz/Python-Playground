from sympy import *

# If an object is dropped from a 155​-foot-high ​building, its position​ (in feet above the​ ground) is given by ​s(t)​, where t is the time in seconds since it was dropped.

t = symbols( 't' )
S = -16*t**2 + 155

dS = diff( S, t )

# The​ object's velocity 1 second after being dropped is 
one_s = dS.subs( { t: 1 } )
one_s

# The object will hit the ground in:
ground = solve( S, t )[ 1 ].evalf()
# ​(Round to the nearest tenth as​ needed.)
round( ground, 1 )

# The​ object's velocity upon impact is:
impact_velocity = dS.subs( { t: ground } )
# (Round to the nearest tenth as​ needed.)
round( impact_velocity, 1 )