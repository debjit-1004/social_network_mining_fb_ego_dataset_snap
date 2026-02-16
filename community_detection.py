import random


def label_propagation_raw(graph, max_iter=20):
    """
    Raw implementation of Label Propagation Algorithm (LPA)
    """
    #  Initialize each node with a unique label
    labels = {node: node for node in graph.nodes()}

    #  Iterate
    for _ in range(max_iter):
        nodes = list(graph.nodes())
        random.shuffle(nodes)

        for node in nodes:
            neighbor_labels = []

            for neighbor in graph.neighbors(node):
                neighbor_labels.append(labels[neighbor])

            if neighbor_labels:
                # Assign the most frequent label among neighbors
                labels[node] = max(
                    set(neighbor_labels),
                    key=neighbor_labels.count
                )

    return labels





