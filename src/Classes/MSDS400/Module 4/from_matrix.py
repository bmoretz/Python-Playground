import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def show_graph_with_labels(adjacency_matrix, mylabels):
	rows, cols = np.where(adjacency_matrix == 1)
	edges = zip( rows.tolist(), cols.tolist() )
	g = nx.Graph()
	g.add_edges_from(edges)
	nx.draw(g, node_size=500, labels=mylabels, with_labels=True)
	return g

A = np.matrix( [ \
	[ 0, 1, 0, 1, 0, 0 ], \
	[ 1, 0, 0, 1, 1, 1  ], \
	[ 0, 0, 0, 0, 1, 1 ], \
	[ 1, 1, 0, 0, 1, 0 ], \
	[ 0, 1, 0, 1, 0, 1 ], \
	[ 0, 1, 1, 1, 1, 0 ], \
	] )

labels={}
labels[0]=r'$a$'
labels[1]=r'$b$'
labels[2]=r'$c$'
labels[3]=r'$d$'
labels[4]=r'$e$'
labels[5]=r'$f$'

G = show_graph_with_labels( A, labels )

plt.show()

if __name__ == '__main__':
	print( 'Number of vertices {0}'.format( G.number_of_nodes() ) )
	print( 'Number of edges {0}'.format( G.number_of_edges() ) )
	print( 'Number of loops {0}'.format( G.number_of_selfloops() ) )

	paths = nx.all_simple_paths( G, source = 0, target = 2 )

	longest = 0

	for p in paths:
		l = len( p )

		if( longest < l ):
			longest = l

	print( 'Longest Path {0}'.format( longest ) )