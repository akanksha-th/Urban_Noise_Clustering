from flask import Blueprint, render_template

charts_bp = Blueprint("charts", __name__, template_folder="../templates")

@charts_bp.route("/charts")
def charts():
    images = [
        {"title": "Complaints Per day_of_week", "file": "time_trends/by_day_of_week.png"},
        {"title": "Complaints Per Hour", "file": "time_trends/by_hour.png"},
        {"title": "Complaints Per Month", "file": "time_trends/by_month.png"},
        {"title": "Complaints Per Year", "file": "time_trends/by_year.png"},
        {"title": "Complaints per Borough", "file": "by_borough.png"},
        {"title": "Noise Complaints by Type", "file": "by_complaint_type.png"},
    ]
    return render_template("charts.html", images=images)