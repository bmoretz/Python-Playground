import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.petersen_graph()

A = nx.incidence_matrix(G)
print(A.todense())

nx.draw_networkx(G)
plt.show()