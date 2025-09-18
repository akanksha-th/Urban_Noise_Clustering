# Urban Noise Clustering

This project builds a scalable ML pipeline for clustering urban noise patterns using a larger dataset. It demonstrates cloud development, orchestration, experiment tracking, and deployment with modern MLOps tools.

---

## Project Folders

    urban_noise_clustering/
    │
    ├── data/                   # sample datasets, input/output
    ├── notebooks/              # experiments, EDA, scratch work
    ├── src/                    # core package
    │   ├── __init__.py
    │   ├── data_prep.py        # Data cleaning + preprocessing
    │   ├── clustering/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── kmeans_cluster.py
    │   │   ├── dbscan_cluster.py
    │   │   └── ensemble.py
    │   ├── evaluation.py       # Metrics, silhouette, etc.
    │   ├── visualization.py    # Plotting functions
    │   └── utils.py            # Helpers (config, logging, etc.)
    │
    ├── app/                    
    │   ├── streamlit_app.py    # Main Streamlit UI
    │   └── components/         # reusable UI components
    │
    ├── tests/                  # unit tests for each module
    ├── requirements.txt
    ├── README.md
    ├── setup.py (optional)     # if making pip-installable
    └── pipeline.py 


⚠️ This project uses Git LFS to store the dataset.
Run 'git lfs install' before cloning to download the dataset automatically.

---

## Project Highlights

- Dagster: orchestrates data pipelines (ETL → preprocessing → clustering → results).
- Gitpod (Cloud Dev): reproducible dev environment in the cloud (no local setup).
- ZenML: defines the ML pipeline steps (data cleaning, clustering, evaluation).
- MLflow: logs experiments, clustering metrics, and artifacts.
- AWS Deployment: scalable deployment of clustering results as an API or dashboard.
- Use Case: unsupervised learning — cluster noise recordings from urban environments to analyze sound patterns.

---

## Tech Stack

Dagster (workflow orchestration)
Gitpod (cloud dev environment)
ZenML (ML pipeline structure)
MLflow (experiment tracking & registry)
AWS (S3, EC2, or Lambda) for deployment
Scikit-learn (KMeans, DBSCAN, PCA)
Python, Pandas, Numpy

---

## How to Run

# Open in Gitpod (cloud dev)
https://gitpod.io/#<repo-url>

# Inside Gitpod, install dependencies
pip install -r requirements.txt

# Run Dagster pipeline
dagster dev

# Run MLflow tracking
mlflow ui
