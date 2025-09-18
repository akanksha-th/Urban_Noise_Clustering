import folium
from folium.plugins import HeatMap
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt


class EDA:
    def __init__(self, df: pd.DataFrame):
        self._df = df.copy()

    def _plot_time_trends(self, ax=None):
        pass

    def _plot_borough_distribution(self, ax=None):
        pass

    def _plot_complaint_types(self, top_n=10, ax=None):
        pass

    def run_eda(self):
        fig, ax = plt.subplots(1, 3, figsize=(20,12))

        self._plot_time_trends(self._df, ax=ax[0])
        self._plot_borough_distribution(self._df, ax=ax[1])
        self._plot_complaint_types(self._df, ax=ax[2])
    

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
    df = pd.read_csv(".data/processed/noise_data_cleaned.csv")
    os.makedirs("outputs", exist_ok=True)

    # eda = EDA(df)
    # plots = eda.run_eda()
    # plot.save("outputs/eda_plots.png")

    geoeda = GeoEDA(df)
    heatmap = geoeda.plot_heatmap()
    heatmap.save("outputs/noise_heatmap.html")