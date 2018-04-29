import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

# Draws a Complete Graph ( K ) with N nodes, Kn
# This graph is bipartite when n >= 3 and even

nodes = 5

G = nx.complete_graph( nodes )

nx.draw_networkx(G)
plt.show()

bipartite.is_bipartite( G )