from flask import Blueprint, render_template, url_for
import os

map_bp = Blueprint("map", __name__, template_folder="../templates")

@map_bp.route("/map")
def map_view():
    folium_path = url_for("static", filename="../outputs/noise_heatmap.html")
    return render_template("map.html", folium_path=folium_path)