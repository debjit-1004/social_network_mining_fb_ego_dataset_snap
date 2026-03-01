import matplotlib.pyplot as plt
import networkx as nx

def plot_degree_dist(G, filename="graph_degree.png"):
    degrees = [d for _, d in G.degree()]
    
    plt.figure()
    plt.hist(degrees, bins=20)
    plt.title("Degree Distribution of Facebook Subgraph")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    
    plt.savefig(filename)
    print(f"saved degree plot to {filename}")

def plot_graph_communities(G, partition, filename="graph_communities.png"):
    if not partition:
        print("no partition data, skipping community plot")
        return

    num_groups = len(set(partition.values()))
    colors = [partition[n] for n in G.nodes()]
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, 
            node_size=40, 
            node_color=colors, 
            cmap=plt.cm.jet, 
            with_labels=False)
            
    plt.title(f"Facebook Network Communities - {num_groups} Groups")
    plt.axis('off')
    plt.savefig(filename)
    print(f"saved community graph to {filename}")

def plot_basic_graph(G, filename="graph.png"):
    plt.figure(figsize=(8, 8))
    nx.draw(G, node_size=40, with_labels=False)
    plt.title("Facebook Social Network (Basic)")
    plt.savefig(filename)
    print(f"saved basic graph to {filename}")
