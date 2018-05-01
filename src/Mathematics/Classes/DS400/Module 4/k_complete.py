import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

# Draws a Complete Graph ( K ) with N nodes, Kn
# This graph is bipartite when n >= 3 and even

nodes = 5

G = nx.complete_graph( nodes )

paths = nx.all_simple_paths(G, source=0, target=3, cutoff=2)
print(list(paths))

nx.draw_networkx(G)
plt.show()

bipartite.is_bipartite( G )