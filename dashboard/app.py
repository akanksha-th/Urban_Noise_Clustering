from flask import Flask, send_from_directory
from pages.home import home_bp
from pages.charts import charts_bp
from pages.map import map_bp
import os

app = Flask(__name__)

@app.route("/outputs/<path:filename>")
def outputs_static(filename):
    return send_from_directory(os.path.join(app.root_path, "../outputs"), filename)

app.register_blueprint(home_bp)
app.register_blueprint(charts_bp)
app.register_blueprint(map_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2346, debug=True)