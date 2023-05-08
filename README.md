# Delivery Time Prediction
=======================================================================

* I have developed a state-of-the-art machine learning model that is capable of accurately predicting the delivery time of the delivery person. Additionally, I have implemented modular coding techniques to streamline the pipelines, allowing the system to be executed using a single python file. Furthermore, The code is able to generate artifacts and logs, providing the  valuable insights into its performance.

## logs

[Check Logs: Link](https://github.com/dev-hack95/delivery_time_prediction/blob/main/logs/25_04_2023_12_09_11.log/25_04_2023_12_09_11.log)

## Run 

1) Initialize git

```bash
git init
```


2) Clone the project

```bash
git clone https://github.com/dev-hack95/delivery_time_prediction
```

3) enter the project directory

```bash
cd delivery_time_prediction
```

4) install the requriments

```bash
pip install -r requirements.txt
```

5) run(By running this file artifacts will automatically generated)

```bash
python src/pipeline/training_pipeline.py
```

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── artifacts          <- For Saving model and processor pipeline pickle files
    │
    ├── notebooks          <- Jupyter notebooks
    │                     
    │                        
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── data_ingestion <- Scripts to turn raw data into features for modeling and data transformation
    |   |   ├── data_ingestion.py
    │   │   └── data_transform.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    |   ├── pipeline       <- Pipelines to train train and predict
    │   │   │
    │   │   ├── prediction_pipeline.py
    │   │   └── training_pipeline.py
    |   |
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   |    └── visualize.py
    │   |
    |   ├── exception.py   <- Script handle sys exceptions
    |   |
    |   ├── logger.py      <- Script handle logging data to logs
    |   |                  
    |   └── utils.py
    |
    |
    |
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
