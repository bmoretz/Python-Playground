import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

# Draws a Wheel Graph ( W ) with N nodes, Wn
# This graph is not bipartite
# This graph has no Euler circuit at any degree.

nodes = 4

G = nx.wheel_graph( nodes )

G.nodes()
G.edges()

bipartite.is_bipartite( G )
nx.draw_networkx(G)
plt.show()