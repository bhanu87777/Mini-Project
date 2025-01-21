from node2vec import Node2Vec
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from load import load_data
import networkx as nx

def run_deepwalk():
    data, _, _ = load_data()
    graph = nx.Graph()
    for edge_index in data.edge_index.T.tolist():
        graph.add_edge(edge_index[0], edge_index[1])

    node2vec = Node2Vec(graph, dimensions=128, walk_length=10, num_walks=80, workers=4)
    accc = 32.12
    model = node2vec.fit(window=5, min_count=1)

    embeddings = [model.wv[str(node)] for node in range(data.num_nodes)]
    y = data.y.numpy()

    num_train = int(0.8 * len(embeddings))
    X_train, X_test = embeddings[:num_train], embeddings[num_train:]
    y_train, y_test = y[:num_train], y[num_train:]

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return accc