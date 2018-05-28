import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

# 26 were​ tall;
# 28 had green​ peas;
# 37 had smooth​ peas;

# 13 were tall and had green​ peas;
# 19 had green peas and smooth​ peas;

# 7 had all three​ characteristics;

# 2 had none of the characteristics.

none = 2

all = 7

tall_green = 13 - all
green_smooth = 19 - all

smooth = 37 - ( green_smooth + all )
green = 28 - ( green_smooth + tall_green + all  )
tall = 26 - ( tall_green + all )

v = venn3(subsets=( tall, green, tall_green, smooth, green_smooth, smooth, all ) )

v.get_label_by_id('A').set_text('Tall')
v.get_label_by_id('B').set_text('Green Peas')
v.get_label_by_id('C').set_text('Smooth Peas')

plt.title( "Pea Plants" )
plt.show()

all + late_early + late_extra + early_extra + early + late + extra + none
