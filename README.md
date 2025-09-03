# Urban Noise Clustering

This project builds a scalable ML pipeline for clustering urban noise patterns using a larger dataset. It demonstrates cloud development, orchestration, experiment tracking, and deployment with modern MLOps tools.

---

## Project Folders

    │   .gitignore
    │   LICENSE
    │   README.md
    │   requirements.txt
    │   run_deployment.py
    │   run_pipeline.py
    │   setup.py
    │
    ├───.github
    │   └───workflows
    │           .gitkeep
    │
    ├───analysis
    │   │   eda_and_fe.ipynb
    │   │
    │   └───analyze_src
    │           bivariate_analysis.py
    │           cluster_diagnostics.py
    │           missing_value_analysis.py
    │           multivariate_analysis.py
    │           univariate_analysis.py
    │           __init__.py
    │
    ├───data
    │       .gitkeep
    │
    ├───pipelines
    │       deployment_pipeline.py
    │       training_pipeline.py
    │       __init__.py
    │
    ├───project_utils
    │       init_project.py
    │
    ├───src
    │       data_cleaning.py
    │       data_ingester.py
    │       data_splitter.py
    │       feature_selection.py
    │       feature_transformation.py
    │       model_building.py
    │       __init__.py
    │
    └───steps
            data_cleaning_step.py
            data_ingester_step.py
            data_splitter_step.py
            feature_selection_step.py
            feature_transformation_step.py
            model_building_step.py
            model_evaluator_step.py
            __init__.py

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
