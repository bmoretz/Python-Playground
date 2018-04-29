import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

# Draws a Cycle Graph ( C ) with N nodes
# bipartite for nodes >= 3 and Even
# Euler Circuit for Nodes > 1 and odd

nodes = 3

G = nx.cycle_graph( nodes )

nx.draw_networkx(G)
plt.show()

print( 'is bipartite: {0}'.format( bipartite.is_bipartite( G ) ) )
[u for u,v in nx.eulerian_circuit(G)]