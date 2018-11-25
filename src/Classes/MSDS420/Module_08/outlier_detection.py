import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(42)

means = 10, 20, 15
stdevs = 4, 2, 3

dist = pd.DataFrame(
    np.random.normal(loc=means, scale=stdevs, size=(1000, 3)),
    columns=['A', 'B', 'C'])

dist.head()

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12,8))

# Pandas
dist.plot.hist(bins=6, title='Pandas Overlap Histogram', ax=ax1)
dist.plot(kind='box', title='Pandas Box Plot', grid=False, ax=ax2)

# Seaborn
sns.set(style="white", palette="muted")

sns.distplot(dist['B'], ax = ax3).set_title('Seaborn "B" Series Histogram')
sns.boxplot(data = dist, ax = ax4).set_title('Seaborn Box Plot')

plt.tight_layout()
plt.show()