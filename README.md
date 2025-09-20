# Urban Noise Clustering

This project builds a scalable ML pipeline for clustering urban noise patterns in New York City using 311 Service Requests dataset.

The key features are:
    - Reproducible pipeline orchestration
    - Interactive Flask dashboard for visual analytics

---

## Project Folders

    urban_noise_clustering/
    │
    ├── .data/                  # raw & processed datasets
    │                 
    ├── notebooks/   
    │   ├── 00.data_lookup.ipynb
    │   ├── 01.data_exploration.ipynb
    │   └── 02.eda.ipynb 
    │ 
    ├── outputs/   
    │   ├── results/
    │   └── # saved visualizations 
    │          
    ├── src/                    # core package
    │   ├── __init__.py
    │   ├── clustering/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   └── ensemble.py
    │   ├── data_prep.py        
    │   ├── feature_engg.py       
    │   ├── visualization.py    
    │   └── utils.py            
    │
    ├── dashboard/                    
    │   ├── app.py    
    │   ├── pages/
    │   │   ├── __init__.py
    │   │   ├── home.py
    │   │   ├── charts.py
    │   │   └── map.py  
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── home.html
    │   │   ├── charts.html     
    │   │   └── map.html     
    │   └── static/      
    │       └── styles.css        
    │
    ├── requirements.txt
    ├── README.md
    └── pipeline.py 


To rerun the pipeline on your local PC, kindly download the dataset from the following website: https://data.cityofnewyork.us/Social-Services/311-Noise-Complaints/p5f6-bkga/about_data

---

## Installation

### Clone the repo
```bash
git clone <git-repo-url>
cd Urban_Noise_Clustering
```

### Set up virtual environment
```bash
python -m venv .clustering_venv
.clustering_venv\Scripts\activate       # Windows
source .clustering_venv/bin/activate    # Linux/Mac
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Running the pipeline
Run the full ML pipeline (data prep → features → visualizations → clustering):
```bash
python pipeline.py
```
Artifacts produced:

    - Processed dataset → .data/processed/
    - Clustering results → outputs/results/
    - Visualizations → outputs/*.png, *.html

### Launch the Dashboard
```bash
cd dashboard
python app.py
```

## Dashboard Preview

![Dashboard](dashboard/static/dashboard.gif)