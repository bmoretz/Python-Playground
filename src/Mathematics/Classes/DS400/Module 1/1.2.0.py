import matplotlib.pyplot
from matplotlib.pyplot import *
import numpy
from numpy import linspace

def plot_line( x1, y1, x2, y2 ):

	slope= (y2-y1) / (x2-x1)

	x= 1.0
	y = y1 + slope*(x-x1)
	print('\nValue of y if x is 1.0 equals {}'.format(y))

	equation = str('y = y1 + slope*(x-x1)')

	x= linspace(-1,8,100)
	y = 6.0 - 1.5*x 
	title('Plot of Linear Equation  '+equation) 
	plot(x,y)
	show()

def break_even_example():
	x= linspace(0,50,100)
	y= 20*x+100.0
	z= 24*x
	figure()  
	plot (x,y)
	plot (x,z)
	legend (('cost','revenue'),loc=2)
	title ('Breakeven Analysis')
	show()

	# p = [ [ 5.0, 4.0 ] , [ -10.0, -2.0 ] ]
	# plot_line( p[ 0 ][ 0 ], p[ 0 ][ 1 ], p[ 1 ][ 0 ], p[ 1 ][ 1 ] )

	# break_even_example()

