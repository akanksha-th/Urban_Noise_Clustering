import os
import pandas as pd
import numpy as np

from src import (
    DataLoader, Preprocess, 
    group_complaints, build_pipeline,
)
from src.clustering import BaseLine, ClusterEnsemble

def main():
    # Data Ingestion
    data_path = ".data/311_Service_Requests_from_2010_to_Present_20250720.csv"
    if not os.path.exists(data_path):
        raise FileNotFoundError("Data File Not Found")
    print("Loading Dataset...")
    loader = DataLoader()
    df = loader.load_data()
    print("Loading Completed!")
    print("---")

    # Data Preprocessing
    print("Preprocessing Data...")
    preprocessor = Preprocess(df)
    processed_df = preprocessor.run_preprocessor()
    processed_df = group_complaints(processed_df)
    # os.makedirs(".data/processed", exist_ok=True)
    # processed_df.to_csv(".data/processed/final_noise_data.csv", index=False)
    print("Preprocessing Completed!")
    print("---")

    # Feature Engineering
    print("Beginning Feature Engineering...")
    feature_pipeline = build_pipeline()
    X = feature_pipeline.fit_transform(processed_df)
    # np.save(".data/processed/noise_feature_matrix.npy", X)
    print("Feature Engineering Completed!")
    print("---")

    # Baseline Models
    print("Running baseline clustering models...")
    base = BaseLine(X)
    baseline_metrics, all_labels = base.run_baseline_models(X)
    print("\nBaseline Model Metrics:")
    for model, vals in baseline_metrics.items():
        print(f"{model}: {vals}")

    # Ensemble Models
    print("Running ensemble clustering models...")
    ensemble = ClusterEnsemble(X)

    # Save Outputs
    output_dir = "outputs/results"
    os.makedirs(output_dir, exist_ok=True)
    
    # save metrics


    print(f"\nPipeline completed. Results saved in: {output_dir}")


if __name__ == "__main__":
    main()