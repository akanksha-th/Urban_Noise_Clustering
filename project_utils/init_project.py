import os
import logging
from pathlib import Path
import subprocess

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]: %(message)s')
logging.info("Creating project scaffold.")

list_of_files = [
    ".github/workflows/.gitkeep",

    "data/.gitkeep",

    "analysis/eda_and_fe.ipynb",
    "analysis/analyze_src/__init__.py",
    "analysis/analyze_src/univariate_analysis.py",
    "analysis/analyze_src/bivariate_analysis.py",
    "analysis/analyze_src/multivariate_analysis.py",
    "analysis/analyze_src/missing_value_analysis.py",
    "analysis/analyze_src/cluster_diagnostics.py",

    "src/__init__.py",
    "src/data_ingester.py",
    "src/data_cleaning.py",
    "src/feature_transformation.py",
    "src/feature_selection.py",
    "src/data_splitter.py",
    "src/model_building.py",

    "steps/__init__.py",
    "steps/data_ingester_step.py",
    "steps/data_cleaning_step.py",
    "steps/feature_transformation_step.py",
    "steps/feature_selection_step.py",
    "steps/data_splitter_step.py",
    "steps/model_building_step.py",
    "steps/model_evaluator_step.py",

    "pipelines/__init__.py",
    "pipelines/training_pipeline.py",
    "pipelines/deployment_pipeline.py",
    
    ".gitignore",
    "requirements.txt",
    "setup.py",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    
    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created file: {filename}")
    else:
        logging.info(f"File- {filename} already exists.")


if not Path(".git").exists():
    subprocess.run(["git", "init"], check=True)
    logging.info("Initialized a new git repository.")
else:
    logging.info("Git repository already initialized.")