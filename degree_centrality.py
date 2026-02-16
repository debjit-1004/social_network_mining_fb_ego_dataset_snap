import networkx as nx



# -------------------------------
# RAW DEGREE CENTRALITY FUNCTION
# -------------------------------

def degree_centrality_raw(graph):
    """
    Computes degree centrality in raw Python.
    Formula:
        C_D(v) = degree(v) / (n - 1)
    """
    n = graph.number_of_nodes()
    centrality = {}

    for node in graph.nodes():
        degree = len(list(graph.neighbors(node)))
        centrality[node] = degree / (n - 1)

    return centrality


