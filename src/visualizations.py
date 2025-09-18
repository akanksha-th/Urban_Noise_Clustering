import folium
from folium.plugins import HeatMap
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt


class EDA:
    def __init__(self, df: pd.DataFrame, save_path: str = None):
        self._df = df.copy()
        self.save_path = save_path

    def _plot_time_trends(self):
        os.makedirs("outputs/time_trends", exist_ok=True)

        plt.figure(figsize=(12,5))
        sns.countplot(x="month", data=self._df, palette="viridis", hue="noise_category")
        plt.title("Noise Complaints by Month of the Year")
        if self.save_path:
            plt.savefig(os.path.join(self.save_path, "time_trends", "by_month.png"))
            plt.close()
        plt.show()

        plt.figure(figsize=(12,5))
        sns.countplot(x="hour", data=self._df, palette="viridis", hue="noise_category")
        plt.title("Noise Complaints by Hour of Day")
        if self.save_path:
            plt.savefig(os.path.join(self.save_path, "time_trends", "by_hour.png"))
            plt.close()
        plt.show()

        plt.figure(figsize=(12,5))
        sns.countplot(x="day_of_week", data=self._df, order=[
            "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], palette="magma", hue="noise_category")
        plt.title("Noise Complaints by Day of Week")
        if self.save_path:
            plt.savefig(os.path.join(self.save_path, "time_trends", "by_day_of_week.png"))
            plt.close()
        plt.show()

        plt.figure(figsize=(12,5))
        sns.countplot(x="year", data=self._df, palette="viridis", hue="noise_category")
        plt.title("Noise Complaint by Year")
        if self.save_path:
            plt.savefig(os.path.join(self.save_path, "time_trends", "by_year.png"))
            plt.close()
        plt.show()

    def _plot_borough_distribution(self, ax=None):
        if ax is None:
            plt.figure(figsize=(8,5))

        sns.countplot(x="borough", data=self._df, palette="coolwarm", hue="noise_category")
        plt.title("Noise Complaints by Borough")
        if self.save_path:
            plt.savefig(os.path.join(self.save_path, "by_borough.png"))
            plt.close()
        plt.show()

    def _plot_complaint_types(self, top_n=10, ax=None):
        if ax is None:
            plt.figure(figsize=(8,5))

        top_types = self._df["noise_category"].value_counts().head(top_n)
        sns.barplot(x=top_types.values, y=top_types.index, palette="Spectral")
        plt.title("Top Noise Complaints by Complaint Types")
        if self.save_path:
            plt.savefig(os.path.join(self.save_path, "by_complaint_type.png"))
            plt.close()
        plt.show()

    def run_eda(self):
        self._plot_time_trends()
        self._plot_borough_distribution()
        self._plot_complaint_types()
    

class GeoEDA:
    def __init__(self, df: pd.DataFrame):
        self._df = df.copy()

    def plot_heatmap(self, map_center=[40.7128, -74.0060], zoom_start=11):
        """
        Plot NYC heatmap of Noise Complaints
        """
        m = folium.Map(location=map_center, zoom_start=zoom_start)
        heat_data = self._df[["latitude", "longitude"]].dropna().values.tolist()
        HeatMap(heat_data, radius=8).add_to(m)
        return m
    

if __name__ == "__main__":
    df = pd.read_csv(".data/processed/final_noise_data.csv")
    os.makedirs("outputs", exist_ok=True)
    save_path = "outputs"

    eda = EDA(df, save_path)
    eda.run_eda()

    geoeda = GeoEDA(df)
    heatmap = geoeda.plot_heatmap()
    heatmap.save("outputs/noise_heatmap.html")