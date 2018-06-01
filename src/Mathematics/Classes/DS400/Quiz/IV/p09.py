import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
from sympy import ( symbols, solve, FiniteSet )

# Total:
# 26 were​ tall;
# 28 had green​ peas;
# 37 had smooth​ peas;

# 13 were tall and had green​ peas;
# 19 had green peas and smooth​ peas;

# 7 had all three​ characteristics;

# 2 had none of the characteristics.

x = symbols( 'x' )

total = 55
none = 2

C = total - none

all = 7

green_smooth = 19
tall_green = 13
tall_smooth = all + x

smooth = 37
green = 28
tall = 26

U = tall + green + smooth - ( tall_green + green_smooth + tall_smooth + all )

ts = solve( U - C, x )[ 0 ]

tall_smooth = tall_smooth.subs( { x: ts } )

A = all 

T = tall - ( tall_smooth + tall_green - all )
G = green - ( green_smooth + tall_green - all )
S = smooth - ( tall_smooth + green_smooth - all )

TG = tall_green
TS = tall_smooth
GS = green_smooth

# Number of plants Tall + Smooth
tall_smooth

v = venn3( subsets=( T, TG, G, GS, S, TS, A ) )

v.get_label_by_id('A').set_text('Tall')
v.get_label_by_id('B').set_text('Green Peas')
v.get_label_by_id('C').set_text('Smooth Peas')

plt.title( "Pea Plants" )
plt.show()