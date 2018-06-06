'''
Vinn diagram for set visualization
'''

from matplotlib import pyplot as plt
from matplotlib_venn import vinn2
from sympy import FiniteSet

set1 = FiniteSet( 1, 3, 5, 7, 9, 11, 15, 17, 19 )
set2 = FiniteSet( 2, 3, 5, 7, 11, 13, 17, 19 )

venn2([set1, set2], ('S', 'T'))
plt.show()

if __name__ == "__main__":
    pass