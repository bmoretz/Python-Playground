import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
from sympy import ( symbols, solve )

x = symbols( 'x' )

U = 52
N = 2

C = U - N

A = 4

TGx = 8
SGx = 16
TSx = x + A

Tx = 20
Gx = 28
Sx = 36

TS = solve( ( Tx + Gx + Sx - SGx - TGx - TSx - A ) - C, x )[ 0 ]
TG = TGx - A
SG = SGx - A

T = Tx - TS - TG - A
G = Gx - SG - TG - A
S = Sx - SG - TS - A

v = venn3( subsets=( T, G, TG, S, TS, SG, A ) )

v.get_label_by_id('A').set_text('Tall')
v.get_label_by_id('B').set_text('Green Peas')
v.get_label_by_id('C').set_text('Smooth Peas')

plt.title( "Pea Plants" )
plt.show()