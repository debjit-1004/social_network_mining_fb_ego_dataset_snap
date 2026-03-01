import networkx as nx
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score

def link_prediction_pipeline(graph):
    print("\nStarting Link Prediction Analysis...")
    
    # 1. generate positive samples (existing edges)
    # label = 1
    positive_links = list(graph.edges())
    
    # 2. generate negative samples (non-existing edges)
    # label = 0
    negative_links = []
    all_nodes = list(graph.nodes())
    num_neg = len(positive_links)
    
    while len(negative_links) < num_neg:
        u = random.choice(all_nodes)
        v = random.choice(all_nodes)
        if u != v and not graph.has_edge(u, v) and (u, v) not in negative_links:
            negative_links.append((u, v))
            
    # combine
    links = positive_links + negative_links
    labels = [1] * len(positive_links) + [0] * len(negative_links)
    
    # 3. feature extraction
    data = []
    
    # generators for scores
    preds_jaccard = nx.jaccard_coefficient(graph, links)
    preds_pref_attach = nx.preferential_attachment(graph, links)
    preds_resource = nx.resource_allocation_index(graph, links)
    
    # map to dicts for easy lookup
    jaccard_scores = {(u, v): p for u, v, p in preds_jaccard}
    pref_scores = {(u, v): p for u, v, p in preds_pref_attach}
    resource_scores = {(u, v): p for u, v, p in preds_resource}
    
    for u, v in links:
        jc = jaccard_scores.get((u, v), jaccard_scores.get((v, u), 0))
        pa = pref_scores.get((u, v), pref_scores.get((v, u), 0))
        ra = resource_scores.get((u, v), resource_scores.get((v, u), 0))
        
        deg_sum = graph.degree(u) + graph.degree(v)
        
        data.append([jc, pa, ra, deg_sum])
        
    # 4. split
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)
    
    # 5. train
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # 6. eval
    preds = clf.predict(X_test)
    probs = clf.predict_proba(X_test)[:, 1]
    
    acc = accuracy_score(y_test, preds)
    auc = roc_auc_score(y_test, probs)
    
    print(f"Link Prediction Accuracy: {acc:.4f}")
    print(f"AUC-ROC: {auc:.4f}")
    
    # feature importance
    importances = clf.feature_importances_
    features = ["Jaccard", "Pref. Attach", "Resource Alloc", "Degree Sum"]
    print("feature importance:")
    for n, i in zip(features, importances):
        print(f"  {n}: {i:.4f}")
        
    return clf
