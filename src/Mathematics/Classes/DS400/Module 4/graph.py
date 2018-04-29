import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from( [ (0,1 ), (2, 3), (4, 1) ] )

nx.draw_networkx(G)
plt.show()

A = nx.adjacency_matrix( G )
print( A.todense() )