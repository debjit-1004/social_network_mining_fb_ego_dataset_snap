import networkx as nx
import time

def check_scalability(original_G):
    print("\n--- checking if my pc explodes (scalability test) ---")
    
    sizes = [100, 500, 1000]
    
    for s in sizes:
        if s > original_G.number_of_nodes():
            break
            
        # grab subset
        nodes = list(original_G.nodes())[:s]
        sub = original_G.subgraph(nodes)
        
        start = time.time()
        
        # betweenness centrality is O(nm) or O(nm + n^2 log n)
        # k=min makes it approx
        _ = nx.betweenness_centrality(sub, k=min(100, s)) 
        
        end = time.time()
        
        print(f"did {s} nodes in {end - start:.4f} seconds")
