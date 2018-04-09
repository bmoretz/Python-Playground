
import matplotlib.pyplot
from matplotlib.pyplot import *
import numpy 
from numpy import linspace

x= linspace(-1,15,100)
y1= 115.0/10.0 - (3.0/10.0)*x
y2= 95.0/4.0 - (11.0/4.0)*x

xlabel('x-axis')
ylabel('y-axis')
plot (x, y1, 'r')
plot (x, y2, 'b')
legend (('3x+10y=115','11x+4y=95'),loc=3)
title ('Solving a System of Equations with a Unique Solution')
show()

x= linspace(0,6,100)
y1= 6.0/(-3.0)+(2.0/3.0)*x
y2= 8.0/6.0 +(4.0/6.0)*x
figure()
plot (x, y1)
plot (x, y2)
xlabel('x-axis')
ylabel('y-axis')
title ('Showing an Inconsistent System of Equations')
show()

x= linspace(0,2,100)
y1= 2.0 - x**2
y2= x**2
figure()
plot (x, y1)
plot (x, y2)
xlabel('x-axis')
ylabel('y-axis')
title ('Showing a Consistent System of Non-linear Equations')
show()

x=linspace(0,100,100)
y=x*x+x
y1=y+1000.0
figure()
xlabel('x-axis')
ylabel('Y-axis')
title ('Plot Showing Inconsistent Nonlinear Equations')
plot(x,y, c='b')
plot(x,y1,c='r')
legend(('y=x**2+x','y=x**2+x+1000'),loc='best') # If loc='best' is used, Python will pick the best location for the legend.
show()


