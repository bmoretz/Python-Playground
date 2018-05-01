import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

A = np.matrix( [ \
	[ 0, 1, 0, 1, 0, 0 ], \
	[ 1, 0, 0, 1, 1, 1  ], \
	[ 0, 0, 0, 0, 1, 1 ], \
	[ 1, 1, 0, 0, 1, 0 ], \
	[ 0, 1, 0, 1, 0, 1 ], \
	[ 0, 1, 1, 1, 1, 0 ], \
	] )

G = nx.from_numpy_matrix(A)

nx.draw_networkx(G)
plt.show()

print( 'Number of vertices {0}'.format( G.number_of_nodes() ) )
print( 'Number of edges {0}'.format( G.number_of_edges() ) )
print( 'Number of loops {0}'.format( G.number_of_selfloops() ) )

paths = nx.all_simple_paths( G, source = 0, target = 2 )

for p in paths:
	print( len( p ) )