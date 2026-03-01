import networkx as nx
import matplotlib.pyplot as plt
import os

import utils
import analysis
import visualization
import scalability
from link_prediction import link_prediction_pipeline

def main():
    # load data
    file_path = "facebook_combined.txt"
    G = utils.load_graph(file_path)

    print("total nodes:", G.number_of_nodes())
    print("total edges:", G.number_of_edges())

    # create subgraph (200 nodes)
    nodes_count = int(os.getenv("subgraph_nodes", 200))
    G_small = utils.get_subgraph(G, nodes_count)

    print("subgraph nodes:", G_small.number_of_nodes())
    print("subgraph edges:", G_small.number_of_edges())

    # basic stats & plots
    visualization.plot_degree_dist(G_small)
    analysis.calculate_basic_stats(G_small)

    # influence & centrality
    analysis.find_top_influencers(G_small)
    analysis.find_connectors(G_small)

    # community detection
    partition, num_comms = analysis.detect_communities(G_small)
    visualization.plot_graph_communities(G_small, partition)
    visualization.plot_basic_graph(G_small)

    # link prediction
    link_prediction_pipeline(G_small)

    # scalability
    scalability.check_scalability(G)

if __name__ == "__main__":
    main()
