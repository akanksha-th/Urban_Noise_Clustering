import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class FeatureEngineer(BaseEstimator, TransformerMixin):
    """Custom transformer for feature engineering"""

    def _cyclic_encode(self, df):
        df = df.copy()
        df["hour_sin"] = np.sin(2 * np.pi * df["hour"].astype(float) / 24)
        df["hour_cos"] = np.cos(2 * np.pi * df["hour"].astype(float) / 24)

        if df["day_of_week"].dtype == "object":
            day_map = {
                "Monday": 0, "Tuesday": 1, "Wednesday": 2,
                "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
            }
            df["day_of_week"] = df["day_of_week"].map(day_map)

        df["dow_sin"] = np.sin(2 * np.pi * df["day_of_week"] / 7)
        df["dow_cos"] = np.cos(2 * np.pi * df["day_of_week"] / 7)

        df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
        df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)
        return df

    def transform(self, df):
        df = df.copy()
        if "noise_category" in df.columns:
            df = df.drop(columns=["noise_category"])
        df = self._cyclic_encode(df)

        useful_cols = [
            "descriptor", "borough", 
            "latitude", "longitude",
            "hour_sin", "hour_cos",
            "dow_sin", "dow_cos",
            "month_sin", "month_cos"
        ]
        return df[useful_cols]

    def fit(self, df, y=None):
        return self


def build_pipeline():
    categorical_features = ["descriptor", "borough"]
    numeric_features = ["latitude", "longitude",
                        "hour_sin", "hour_cos", 
                        "dow_sin", "dow_cos",
                        "month_sin", "month_cos"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
        ]
    )

    # Full pipeline: feature engineering + preprocessing
    pipeline = Pipeline(steps=[
        ("features", FeatureEngineer()),
        ("preprocess", preprocessor)
    ])

    return pipeline


if __name__ == "__main__":
    df = pd.read_csv(".data/processed/final_noise_data.csv")

    pipeline = build_pipeline()
    X = pipeline.fit_transform(df)

    print("Transformed shape:", X.shape)

    # Save as binary
    np.save(".data/processed/noise_feature_matrix.npy", 
            X.toarray() if hasattr(X, "toarray") else X)
