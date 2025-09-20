# Urban Noise Clustering

This project builds a scalable ML pipeline for clustering urban noise patterns using a larger dataset. It demonstrates cloud development, orchestration, experiment tracking, and deployment with modern MLOps tools.

---

## Project Folders

    urban_noise_clustering/
    │
    ├── .data/  
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
    ├── setup.py (optional)     # if making pip-installable
    └── pipeline.py 


To rerun the pipeline on your local PC, kindly download the dataset from the following website: https://data.cityofnewyork.us/Social-Services/311-Noise-Complaints/p5f6-bkga/about_data

---
