import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()

nx.draw_networkx(G)
plt.show()