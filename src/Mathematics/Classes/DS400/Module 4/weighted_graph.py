import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()

G.add_edge('a','b',weight=2)
G.add_edge('b','e',weight=3)
G.add_edge('e','d',weight=2)
G.add_edge('d','a',weight=3)

pos=nx.spring_layout(G) # positions for all nodes

elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

# edges
nx.draw_networkx_edges(G, pos,edgelist=elarge,
                    width=6)

nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')

# labels
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display