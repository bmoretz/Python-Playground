import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

# 35 trucks went out carrying early​ peaches;
# 69 carried late​ peaches;
# 54 carried extra late​ peaches;

# 26 carried early and​ late;
# 31 carried late and extra​ late;
# 7 carried early and extra​ late;

# 2 carried all​ three;

# 8 carried only figs​ (no peaches at​ all).

all = 2

late_early = 26 - all
late_extra = 31 - all
early_extra = 7 - all

early = 35 - ( late_early + early_extra + all )
late = 69 - ( late_extra + late_early + all  )
extra = 54 - ( late_extra + early_extra + all )

v = venn3(subsets=( early, late, late_early, extra, early_extra, late_extra, all ), set_labels = ('E', 'L', 'X'))

v.get_label_by_id('A').set_text('Early')
v.get_label_by_id('B').set_text('Late')
v.get_label_by_id('C').set_text('Extra Late')

plt.title( "Peaches" )
plt.show()

all + late_early + late_extra + early_extra + early + late + extra  + 8