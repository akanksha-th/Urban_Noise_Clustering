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
            df = pd.read_csv(self._filepath)
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

    def clean(self) -> pd.DataFrame:
        # Standardizing column names
        self._df.columns = self._df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Prase datetime
        if "created_date" in self._df.columns:
            self._df["created_date"] = pd.to_datetime(self._df["created_date"], errors="coerce")
        self._df = self._df.dropna(subset=["created_date"])
        return self._df

    def engineer_time_features(self) -> pd.DataFrame:
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


if __name__ == "__main__":
    processed_path = ".data/processed/noise_data_cleaned.csv"

    loader = DataLoader()
    df = loader.load_data()

    preprocessor = Preprocess(df)
    cleaned_df = preprocessor.clean()
    extended_df = preprocessor.engineer_time_features()

    os.makedirs(".data/processed", exist_ok=True)
    extended_df.to_csv(processed_path, index=False)
    print(f"Processed data saved to {processed_path}")