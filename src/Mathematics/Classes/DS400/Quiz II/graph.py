import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()

A = nx.adjacency_matrix(G)
print(A.todense())

nx.draw_networkx(G)
plt.show()