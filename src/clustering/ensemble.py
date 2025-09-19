# src/ensemble.py
import numpy as np
import pandas as pd
from .base import BaseLine


def ensemble_voting(X, cluster_labels_dict):
    """
    Simple ensemble clustering: majority vote across models
    """
    clusterings = np.array(list(cluster_labels_dict.values()))
    n_samples = X.shape[0]
    ensemble_labels = []

    for i in range(n_samples):
        votes = clusterings[:, i]
        votes = votes[votes >= 0]  # ignore noise (-1)
        if len(votes) > 0:
            ensemble_labels.append(np.bincount(votes).argmax())
        else:
            ensemble_labels.append(-1)
    ensemble_labels = np.array(ensemble_labels)

    return base._evaluate_clustering(X, ensemble_labels, "Ensemble"), ensemble_labels


if __name__ == "__main__":
    X = pd.read_csv("")

    base = BaseLine()
    _, all_labels = base.run_baseline_models(X)
    metrics, ensemble_labels = ensemble_voting(X, all_labels)

    print("Ensemble Results:", metrics)
