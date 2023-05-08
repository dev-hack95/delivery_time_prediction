import sys
sys.path.append("./src")
from data_ingestion.data_ingestion import DataIngestion
from data_ingestion.data_transform import DataTransformation
from models.train_model import TrainModel


if __name__ == "__main__":
    train_data_path, test_data_path = DataIngestion().initiate_data_ingestion()
    train_arr, test_arr, _ = DataTransformation().initiate_data_transformation(train_data_path, test_data_path)
    train_model = TrainModel()
    train_model.initiate_model_traing(train_arr, test_arr)