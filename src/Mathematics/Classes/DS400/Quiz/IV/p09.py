import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
from sympy import ( symbols, solve )

x = symbols( 'x' )

U = 54
N = 2

C = U - N

A = 6

TGx = 10
SGx = 18
TSx = x + A

Tx = 22
Gx = 29
Sx = 39

TS = solve( ( Tx + Gx + Sx - SGx - TGx - TSx + A ) - C, x )[ 0 ]
TG = TGx - A
SG = SGx - A

T = Tx - TS - TG - A
G = Gx - SG - TG - A
S = Sx - SG - TS - A

v = venn3( subsets=( T, G, TG, S, TS, SG, A ) )

v.get_label_by_id('A').set_text('Tall')
v.get_label_by_id('B').set_text('Green Peas')
v.get_label_by_id('C').set_text('Smooth Peas')

print( 'Plants that are tall and smooth peas {0}'.format( TS + A ) )
print( 'Plants that are not smooth or green {0}'.format( T ) )
print( 'Plants that are not tall but have smooth AND green peas {0}'.format( SG ) )

plt.title( "Pea Plants" )
plt.show()