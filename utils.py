import networkx as nx
import os

def load_graph(filepath):
    print(f"trying to load graph from {filepath}...")
    G = nx.read_edgelist(filepath, nodetype=int)
    print("got it!")
    return G

def get_subgraph(G, num_nodes=200):
    # take first 'num_nodes' nodes
    nodes = list(G.nodes())[:num_nodes]
    sub = G.subgraph(nodes)
    return sub
