import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

# Draws a Lollipop Graph ( K ) with N nodes, and E edges

nodes = 2
edges = 3

G = nx.lollipop_graph( nodes, edges )

nx.draw_networkx(G)
plt.show()

print( 'is bipartite: {0}'.format( bipartite.is_bipartite( G ) ) )

[u for u,v in nx.eulerian_circuit(G)]

A = nx.adjacency_matrix( G )
print( A.todense() )