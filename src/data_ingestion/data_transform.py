import os
import sys
import pandas as pd
import numpy as np
sys.path.append("./src")
from logger import logging
from exception import CustomException
from utils import save_object
from dataclasses import dataclass
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")



class DataTransformation:
    def __init__(self) -> None:
        self.transformation_config = DataTransformationConfig

    def get_data_transformation_object(self):
        try:
            logging.info("Data Transformation Initiated")

            categorical_columns = ['Weather_conditions', 'Road_traffic_density', 'Type_of_order', 'Type_of_vehicle', 'Festival', 'City']
            numerical_columns = ['Delivery_person_Age', 'Delivery_person_Ratings', 'Displacement']
            
            weather_categories = ['Fog', 'Stormy', 'Sandstorms', 'Windy', 'Cloudy', 'Sunny']
            traffic_density_categories = ['Jam', 'High', 'Medium', 'Low']
            order_categories = ['Snack', 'Meal', 'Drinks', 'Buffet']
            vehicle_categories = ['motorcycle', 'scooter', 'electric_scooter', 'bicycle']
            festival_categories = ['No', 'Yes']
            city_categories = ['Metropolitian', 'Urban', 'Semi-Urban']

            num_pipeline = Pipeline(
                steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder', OrdinalEncoder(categories=[weather_categories, traffic_density_categories, order_categories ,vehicle_categories, festival_categories, city_categories])),
                ('scaler', StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_columns),
                ('cat_pipeline', cat_pipeline, categorical_columns)
            ])

            return preprocessor


        except Exception as error:
            logging.info("Error Occured in Data Transformation")
            raise CustomException(error, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Data transformation initiated")
            train_df = pd.read_csv("data/raw/train.csv")
            test_df = pd.read_csv("data/raw/test.csv")

            logging.info("Read the train and test data")
            logging.info(f"Train Dataframe head: \n{train_df.head().to_string()}")
            logging.info(f"Test Dataframe head: \n{test_df.head().to_string()}")

            logging.info("Getting processing object")

            preprocessor_obj = self.get_data_transformation_object()

            target_column = 'Time_taken (min)'
            drop_columns = [target_column]

            input_column_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_column_train_df = train_df[target_column]

            input_column_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_column_test_df = test_df[target_column]

            input_column_train_arr = preprocessor_obj.fit_transform(input_column_train_df)
            input_column_test_arr = preprocessor_obj.transform(input_column_test_df)

            train_arr = np.c_[input_column_train_arr, np.array(target_column_train_df)]
            test_arr = np.c_[input_column_test_arr, np.array(target_column_test_df)]


            save_object(
                file_path=self.transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )
            logging.info("Data transformation completed")

            return (
                train_arr,
                test_arr,
                self.transformation_config.preprocessor_obj_file_path
            )

        except Exception as error:
            logging.info("Exception occured at initiation of data transformation")
            raise CustomException(error, sys)
        