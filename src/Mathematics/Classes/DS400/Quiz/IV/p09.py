import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

# 26 were​ tall;
# 28 had green​ peas;
# 37 had smooth​ peas;

U = 55
N = 2

C = U - N

A = 7

none = 2

all = 7

green_smooth = 19 - all
tall_green = 13 - all

no_peas = ( green_smooth + tall_green )

smooth = 37 - ( green_smooth + all )
green = 28 - ( green_smooth + tall_green + all  )
tall = 26 - ( tall_green + all )

v = venn3( subsets=( tall, green, tall_green, smooth, green_smooth, smooth, all ) )

v.get_label_by_id('A').set_text('Tall')
v.get_label_by_id('B').set_text('Green Peas')
v.get_label_by_id('C').set_text('Smooth Peas')

print( 'Plants that are tall and smooth peas {0}'.format( TS + A ) )
print( 'Plants that are not smooth or green {0}'.format( T ) )
print( 'Plants that are not tall but have smooth AND green peas {0}'.format( SG ) )

plt.title( "Pea Plants" )
plt.show()

tall = set( { 26 } )
green_peas = set( { 28 } )
smooth_peas = set( { 37 } )

tall 