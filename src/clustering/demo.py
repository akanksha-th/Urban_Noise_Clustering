from tqdm import tqdm
import numpy as np
import os
import json
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score


class ClusterRunner:
    def __init__(self, X, n_clusters=8, eps=0.5, min_samples=10):
        self.X = X
        self.n_clusters = n_clusters
        self.eps = eps
        self.min_samples = min_samples

    def _evaluate(self, labels, name):
        if len(set(labels)) <= 1:
            return {name: {"silhouette": -1, "db_index": np.inf, "calinski": -1}}

        return {
            name: {
                "silhouette": silhouette_score(self.X, labels),
                "db_index": davies_bouldin_score(self.X, labels),
                "calinski": calinski_harabasz_score(self.X, labels),
            }
        }

    def run_kmeans(self):
        km = KMeans(n_clusters=self.n_clusters, random_state=17)
        labels = km.fit_predict(self.X)
        return self._evaluate(labels, "KMeans"), {"KMeans": labels.tolist()}

    def run_gmm(self):
        gmm = GaussianMixture(n_components=self.n_clusters, random_state=17)
        labels = gmm.fit_predict(self.X)
        return self._evaluate(labels, "GMM"), {"GMM": labels.tolist()}

    def run_dbscan(self):
        db = DBSCAN(eps=self.eps, min_samples=self.min_samples)
        labels = db.fit_predict(self.X)
        return self._evaluate(labels, "DBSCAN"), {"DBSCAN": labels.tolist()}


if __name__ == "__main__":
    X = np.load(".data/processed/noise_feature_matrix.npy")
    print(f"Features loaded successfully! Shape: {X.shape}")
    print(X.dtype)
    print(np.isnan(X).sum())

    runner = ClusterRunner(X, n_clusters=5, eps=0.5, min_samples=10)

    all_metrics = {}
    all_labels = {}

    model_list = ["kmeans", "gmm", "dbscan"]

    for method in tqdm(model_list, desc="Running Clustering Baselines"):
        if method == "kmeans":
            metrics, labels = runner.run_kmeans()
        elif method == "gmm":
            metrics, labels = runner.run_gmm()
        elif method == "dbscan":
            metrics, labels = runner.run_dbscan()

        all_metrics.update(metrics)
        all_labels.update(labels)

    print("\nBaseline Results:")
    for model, vals in all_metrics.items():
        print(model, vals)

    os.makedirs("outputs/results", exist_ok=True)
    with open("outputs/results/baseline_metrics.json", "w") as f:
        json.dump(all_metrics, f, indent=4)
    with open("outputs/results/baseline_labels.json", "w") as f:
        json.dump(all_labels, f, indent=4)

    print("\nResults saved in outputs/results/")
