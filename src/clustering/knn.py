import os
import json
import numpy as np
from tqdm import tqdm 
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    #calinkski_harabasz_score
)

class KNNClustering:
    """Batch-wise KNN trainer for baseline model training"""
    def __init__(self,
                 data_path,
                 n_clusters,
                 batch_size=5000,
                 max_iter=150,
                 output_dir="outputs/results/batch_kmeans",
                 random_state=17):
        self.data_path = data_path
        self.n_clusters = n_clusters
        self.batch_size = batch_size
        self.max_iter = max_iter
        self.output_dir = output_dir
        self.random_state = random_state

        self._prepare_output_dir()
        self.model = MiniBatchKMeans(
            n_clusters=self.n_clusters,
            batch_size=self.batch_size,
            max_iter=self.max_iter,
            random_state=self.random_state
        )

    def _prepare_output_dir(self):
        os.makedirs(self.output_dir, exist_ok=True)

    def _load_data_in_batches(self):
        X = np.load(self.data_path)
        n_samples = X.shape[0]
        print(f"Starting batch-wise training on {n_samples} samples (batch={self.batch_size})")

        for start in tqdm(range(0, n_samples, self.batch_size), desc="MiniBatchKmeans"):
            end = min(start + self.batch_size, n_samples)
            batch = X[start:end]
            self.model.partial_fit(batch)

        print("Batch-wise training completed.")

    def evaluate(self, X):
        labels = self.model.predict(X)
        unique_labels = np.unique(labels)

        if len(unique_labels) <= 1:
            return {
            "silhouette_score": -1,
            "davies_bouldin_score": -1,
            #"calinski_harabasz_score": -1
            }
        
        metrics = {
            "silhouette": float(silhouette_score(X, labels)),
            "davies_bouldin": float(davies_bouldin_score(X, labels)),
            #"calinski_harabasz": float(calinkski_harabasz_score(X, labels)),
        }

        return metrics, labels
    
    def save_results(self, metrics, labels):
        metrics_path = os.path.join(self.output_dir, "metrics.json")
        labels_path = os.path.join(self.output_dir, "cluster_labels.npy") 

        with open(metrics_path, "w") as f:
            json.dump(metrics, f, indent=4)
        np.save(labels_path, labels)
        print(f"Results saved in {self.output_dir}/")

    def run(self):
        self._load_data_in_batches()
        X = np.load(self.data_path)
        metrics, labels = self.evaluate(X)
        self.save_results(metrics, labels)
        print("Evaluation Metrics:", metrics)
        return metrics, labels
    

if __name__ == "__main__":
    trainer = KNNClustering(
        data_path=".data/processed/noise_feature_matrix.npy",
        n_clusters=5,
        batch_size=8000,
        max_iter=200,
    )
    trainer.run()