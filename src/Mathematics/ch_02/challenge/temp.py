'''

Weather Compare

'''

from matplotlib import pyplot as plt
from datetime import datetime

import math

def draw_graph( time, temp, city ) :
	plt.plot( time, temp, marker = 'o', label = city )
	plt.xlabel( 'Time' )
	plt.ylabel( 'Temperature' )
	plt.title( ' NYC / Austin Weather' )

def str_to_date( values ):
	tmp = []
	for str in values:
		tmp.append( datetime.strptime( str, '%I:%M %p') )
	return( tmp )

nyc_time = [ '11:30 AM','12:00 PM','01:00 PM','02:00 PM','03:00 PM','04:00 PM','05:00 PM','06:00 PM','07:00 PM','08:00 PM','09:00 PM','10:00 PM','11:00 PM','12:00 AM','01:00 AM','02:00 AM' ]
nyc_time = str_to_date( nyc_time )
nyc_time = sorted( nyc_time )

nyc_temp = ( 47,48,49,49,52,53,55,53,51,53,55,56,57,57,55,53 )

draw_graph( nyc_time, nyc_temp, "NYC" )

austin_time = [ '10:30 AM','11:00 AM','12:00 PM','01:00 PM','02:00 PM','03:00 PM','04:00 PM','05:00 PM','06:00 PM','07:00 PM','08:00 PM','09:00 PM','10:00 PM','11:00 PM','12:00 AM','01:00 AM' ]
austin_time = str_to_date( nyc_time )
austin_time = sorted( nyc_time )

austin_temp = ( 33, 34, 35, 36, 38, 41, 42, 42, 43, 41, 40, 39, 39, 38, 37, 36 )

draw_graph( austin_time, austin_temp, 'Austin' )

plt.legend()
plt.show()