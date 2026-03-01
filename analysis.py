import networkx as nx

# try to import external library, otherwise it will satisfy later in the code
try:
    import community as community_louvain
except ImportError:
    community_louvain = None

def calculate_basic_stats(G):
    # density = 2*E/(N*(N-1))
    den = nx.density(G)
    print("density is:", round(den, 4))
    
    # avg clustering coeff
    avg_clus = nx.average_clustering(G)
    print("clustering coeff:", round(avg_clus, 4))
    return den, avg_clus

def find_top_influencers(G):
    # pagerank (google style ranking)
    pr = nx.pagerank(G)
    
    # sort by score
    top = sorted(pr.items(), key=lambda x: x[1], reverse=True)[:5]
    
    print("\ntop 5 big shots (pagerank):")
    for n, s in top:
        print(f"node {n} has score {s:.4f}")
    
    return top

def find_connectors(G):
    print("\ncalculating betweenness... might take a sec")
    bet = nx.betweenness_centrality(G)
    
    top_bet = sorted(bet.items(), key=lambda x: x[1], reverse=True)[:3]
    print("top 3 bridges:", top_bet)
    return top_bet

def detect_communities(G):
    print("\nlooking for communities...")
    
    part = {}
    try:
        # trying external lib first
        part = community_louvain.best_partition(G)
    except:
        # fallback to networkx builtin if the other one fails
        try:
            print("external lib failed, trying networkx builtin...")
            comms = nx.community.louvain_communities(G)
            for i, c in enumerate(comms):
                for n in c:
                    part[n] = i
        except:
            print("cant find any algo for communities :(")
            
    num = len(set(part.values())) if part else 0
    print(f"found {num} communities")
    
    return part, num
