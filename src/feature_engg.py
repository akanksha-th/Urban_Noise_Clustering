import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class FeatureEngineer(BaseEstimator, TransformerMixin):
    """Custom transformer for feature engineering"""

    def __init__(self):
        self.freq_maps = {}  # to store frequency encodings during fit

    def _cyclic_encode(self, df, col, max_val):
        df[col + "_sin"] = np.sin(2 * np.pi * df[col].astype(float) / max_val)
        df[col + "_cos"] = np.cos(2 * np.pi * df[col].astype(float) / max_val)
        return df

    def fit(self, X, y=None):
        X = X.copy()

        # learn frequency maps
        for col in ["incident_zip", "descriptor", "noise_category"]:
            self.freq_maps[col] = X[col].value_counts(normalize=True).to_dict()

        return self

    def transform(self, X):
        X = X.copy()

        # Ensure correct numeric types
        if X["day_of_week"].dtype == "object":
            day_map = {
                "Monday": 0, "Tuesday": 1, "Wednesday": 2,
                "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
            }
            X["day_of_week"] = X["day_of_week"].map(day_map)

        # cyclic encodings
        X = self._cyclic_encode(X, "hour", 24)
        X = self._cyclic_encode(X, "day_of_week", 7)
        X = self._cyclic_encode(X, "month", 12)

        # apply frequency encoding
        for col in ["incident_zip", "descriptor", "noise_category"]:
            X[col + "_freq"] = X[col].map(self.freq_maps[col]).fillna(0)

        return X


def build_pipeline():
    # define feature groups
    numeric_features = [
        "latitude", "longitude",
        "hour_sin", "hour_cos",
        "day_of_week_sin", "day_of_week_cos",
        "month_sin", "month_cos",
        "incident_zip_freq", "descriptor_freq", "noise_category_freq"
    ]
    numeric_transformer = StandardScaler()

    categorical_features = ["borough"]
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )

    pipeline = Pipeline(steps=[
        ("feature_engineering", FeatureEngineer()),
        ("preprocessor", preprocessor)
    ])

    return pipeline


if __name__ == "__main__":
    df = pd.read_csv(".data/processed/final_noise_data.csv")

    pipeline = build_pipeline()
    X = pipeline.fit_transform(df)

    print("Transformed shape:", X.shape)
    np.save(".data/processed/noise_feature_matrix.npy", X)