import sys
sys.path.append("./src")
from data_ingestion.data_transform import DataTransformation
from data_ingestion.data_ingestion import DataIngestion, DataIngestionConfig
from models.train_model import TrainModel

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline


def register_pipelines(**kwargs) -> Pipeline :
    return pipeline([
        node(
            func=DataIngestion().initiate_data_ingestion(),
            inputs = [],
            outputs = [],
            name="Data Ingestion"
        ),

        node(
            func=DataTransformation().initiate_data_transformation(DataIngestionConfig().train_data_path, DataIngestionConfig().test_data_path),
            name="Data Transformation"
        ),
    ]
    )