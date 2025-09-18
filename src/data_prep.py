import pandas as pd
import os

class DataLoader:
    """
    Loads noise complaint dataset
    """
    def __init__(self, filepath: str = ".data/311_Service_Requests_from_2010_to_Present_20250720.csv"):
        self._filepath = filepath

    def load_data(self) -> pd.DataFrame:
        """
        Load datset into pandas DataFrame
        """
        try:
            df = pd.read_csv(self._filepath, low_memory=False)
            print("Successfully Loaded File!!")
            return df
        except Exception as e:
            print(f"An Error {e} occurred.")
            raise


class Preprocess:
    """
    Cleans and Prepares datase for analysis
    """
    def __init__(self, df: pd.DataFrame):
        self._df = df.copy()

    def _clean(self) -> pd.DataFrame:
        # Standardizing column names
        self._df.columns = self._df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Keep only relevant columns
        keep_cols = [
            "created_date", "complaint_type", "descriptor",
            "borough", "incident_zip", "latitude", "longitude", "status"
        ]
        self._df = self._df[keep_cols]

        # Prase datetime
        if "created_date" in self._df.columns:
            self._df["created_date"] = pd.to_datetime(
                self._df["created_date"], 
                format="%m/%d/%Y %I:%M:%S %p",
                errors="coerce")
        self._df = self._df.dropna(subset=["created_date"])
        return self._df

    def _engineer_time_features(self) -> pd.DataFrame:
        """
        Create time-based features
        """
        if "created_date" in self._df.columns:
            self._df["year"] = self._df["created_date"].dt.year
            self._df["month"] = self._df["created_date"].dt.month
            self._df["day"] = self._df["created_date"].dt.day
            self._df["hour"] = self._df["created_date"].dt.hour
            self._df["day_of_week"] = self._df["created_date"].dt.day_name()

        print("Engineered Time Features")
        return self._df
    
    def _imputer(self) -> pd.DataFrame:
        """
        Impute missing latitude/longitude using zip code centroids
        """
        self._df["borough"] = self._df["borough"].fillna("UNKNOWN")
        self._df = self._df.dropna(subset="incident_zip")

        # Calculate centroid per incident_zip
        zip_centroids = (
            self._df.dropna(subset=["latitude", "longitude"])
            .groupby("incident_zip")[["latitude", "longitude"]]
            .mean()
        )

        # Fill missing lat/long using centroid of the same zip
        def fill_lat(row):
            if pd.isna(row["latitude"]) and row["incident_zip"] in zip_centroids.index:
                return zip_centroids.loc[row["incident_zip"], "latitude"]
            return row["latitude"]

        def fill_long(row):
            if pd.isna(row["longitude"]) and row["incident_zip"] in zip_centroids.index:
                return zip_centroids.loc[row["incident_zip"], "longitude"]
            return row["longitude"]

        self._df["latitude"] = self._df.apply(fill_lat, axis=1)
        self._df["longitude"] = self._df.apply(fill_long, axis=1)

        return self._df
    
    def run_preprocessor(self) -> pd.DataFrame:
        self._clean()
        self._imputer()
        self._engineer_time_features()
        return self._df


if __name__ == "__main__":
    processed_path = ".data/processed/noise_data_cleaned.csv"

    loader = DataLoader()
    df = loader.load_data()

    preprocessor = Preprocess(df)
    extended_df = preprocessor.run_preprocessor()

    os.makedirs(".data/processed", exist_ok=True)
    extended_df.to_csv(processed_path, index=False)
    print(f"Processed data saved to {processed_path}")