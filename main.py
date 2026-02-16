import networkx as nx
import matplotlib.pyplot as plt
import os

from community_detection import label_propagation_raw
from degree_centrality import degree_centrality_raw


G = nx.read_edgelist(
    "facebook_combined.txt",
    nodetype=int
)

print("Total nodes:", G.number_of_nodes())
print("Total edges:", G.number_of_edges())


#   get 200 nodes
nodes= os.getenv("subgraph_nodes")
nodes_200 = list(G.nodes())[:1000]
# GET ALL EDGES CONNECTING THESE 200 NODES
G_small = G.subgraph(nodes_200)

print("Subgraph nodes:", G_small.number_of_nodes())
print("Subgraph edges:", G_small.number_of_edges())


degrees = [deg for _, deg in G_small.degree()]

plt.hist(degrees, bins=20)
plt.title("Degree Distribution of Facebook Subgraph")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.savefig("graph_degree.png")
print("Graph degree saved to graph_degree.png")


# nw density = 2*E/(N*(N-1))
density = nx.density(G_small)
print("Network Density:", round(density, 4))

# nw visualise
plt.figure(figsize=(8, 8))

# 40 IS THE NODE SIZE, WITH_LABELS=False TO HIDE NODE LABELS
nx.draw(G_small, node_size=40, with_labels=False)
plt.title("Facebook Social Network (200 Nodes)")
plt.savefig("graph.png")
print("Graph visualization saved to graph.png")





# Compute degree centrality
degree_centrality = degree_centrality_raw(G_small)

# TOP 5 INFLUENTIAL USERS

top_5 = sorted(
    degree_centrality.items(),
    key=lambda x: x[1],
    reverse=True
)[:5]


# def get_score(item_tuple):
#     return item_tuple[1]  # Return the score

# top_5 = sorted(degree_centrality.items(), key=get_score, reverse=True)

print("Top 5 Influential Users (Raw Degree Centrality):")
for node, score in top_5:
    print(f"Node {node} : {score:.4f}")



# Run community detection
labels = label_propagation_raw(G_small)
# Group nodes by community
communities = {}
for node, label in labels.items():
    communities.setdefault(label, []).append(node)






print("Number of communities detected:", len(communities))

for i, (label, nodes) in enumerate(communities.items(), 1):
    print(f"Community {i}: {len(nodes)} nodes")
