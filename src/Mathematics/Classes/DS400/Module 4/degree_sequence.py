import networkx as nx

z = [ 4, 3, 3, 2, 2 ]

print( nx.is_valid_degree_sequence_erdos_gallai( z ) )

print("Configuration model")
G = configuration_model(z)  # configuration model

degree_sequence = list( nx.degree(G) ) # degree sequence

if __name__ == '__main__':
	print( "Degree sequence %s" % degree_sequence )
	print( 'Nodes: {0}'.format( len( G.nodes() ) ) )
	print( 'Edges: {0}'.format( len( G.edges() ) ) )