import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

# Draws a Hypercube Graph ( Q ) with N nodes, Qn
# This graph is bipartite when n >= 1
# This graph has an Euler Circuit with Nodes > 0 and N is Even

nodes = 2

G = nx.hypercube_graph( nodes )

nx.draw_networkx(G)
plt.show()

print( 'is bipartite: {0}'.format( bipartite.is_bipartite( G ) ) )
[u for u,v in nx.eulerian_circuit(G)]