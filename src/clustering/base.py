import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

class BaseLine:
    def __init__(self, X, n_clusters=8):
        self.X = X
        self.n_clusters = n_clusters

    def _evaluate_clustering(self, X, labels, name):
        if len(set(labels)) <= 1:
            return {name: {"silhouette": -1, "db_index": np.inf, "calinski": -1}}
        return {
            name: {
                "silhouette": silhouette_score(self.X, labels),
                "db_index": davies_bouldin_score(self.X, labels),
                "calinski": calinski_harabasz_score(self.X, labels)
            }
        }
    
    def run_baseline_models(self):
        results = {}
        all_labels ={}

        # KMeans
        km = KMeans(n_clusters=self.n_clusters, random_state=17)
        km_labels = km.fit_predict(self.X)
        results.update(self._evaluate_clustering(self.X, km_labels, "KMeans"))
        all_labels["KMeans"] = km_labels

        # Agglomerative
        agg = AgglomerativeClustering(n_clusters=self.n_clusters)
        agg_labels = agg.fit_predict(self.X)
        results.update(self._evaluate_clustering(self.X, agg_labels, "Agglomerative"))
        all_labels["Agglomerative"] = agg_labels

        # DBSCAN
        db = DBSCAN(eps=0.3, min_samples=10)
        db_labels = db.fit_predict(self.X)
        results.update(self._evaluate_clustering(self.X, db_labels, "DBSCAN"))
        all_labels["DBSCAN"] = db_labels

        return results, all_labels
    
if __name__ == "__main__":
    X = np.load(".data/processed/noise_feature_matrix.npy")

    base = BaseLine(X)
    metrics, labels = base.run_baseline_models()
    print("Baseline Results:")
    for model, vals in metrics.items():
        print(model, vals)