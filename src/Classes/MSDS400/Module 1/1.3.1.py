import matplotlib.pyplot
from matplotlib.pyplot import *

import numpy 
from numpy import linspace

y = 0.086544 * x ** 2 + 0.304694*x

y.subs( { x: 55 } ).evalf()

x = linspace( 0, 100, 100 )
xlabel('x-axis')
ylabel('y-axis')
plot( x, y, 'b' )

# @ 25 mph
mph = 25
plot( mph, y[ mph ], marker='o', markersize=3, color="green" )

# @ 35 mph
mph = 35
plot( mph, y[ mph ], marker='o', markersize=3, color="green" )

# @ 55 mph
mph = 55
plot( mph, y[ mph ], marker='o', markersize=3, color="red" )

legend( ( 'y = ax^2 + bx', '25 mph', '35 mph', '55 mph' ), loc = 'best' )
title( 'Stopping distance of a traveling car' )

show()