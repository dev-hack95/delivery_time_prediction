import os
import sys
sys.path.append("./src")
import pandas as pd
from exception import CustomException
from logger import logging
from utils import load_object

class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data = preprocessor.transform(features)

            pred = model.predict(data)

            return pred

        except Exception as error:
            logging.info("Exception ocuured at prediction")
            CustomException(error, sys)


class CustomData:
    def __init__(self,
                 Delivery_person_Age:float,
                 Delivery_person_Ratings:float,
                 Weather_conditions:str,
                 Road_traffic_density:str,
                 Vehicle_condition:int,
                 Type_of_order:str,
                 Type_of_vehicle:str,
                 multiple_deliveries:float,
                 Festival:str,
                 City:str,
                 Displacement:float) -> None:
        
        self.Delivery_person_Age = Delivery_person_Age
        self.Delivery_person_Ratings = Delivery_person_Ratings
        self.Weather_conditions = Weather_conditions
        self.Road_traffic_density = Road_traffic_density
        self.Vehicle_condition = Vehicle_condition
        self.Type_of_order = Type_of_order
        self.Type_of_vehicle = Type_of_vehicle
        self.multiple_deliveries = multiple_deliveries
        self.Festival = Festival
        self.City = City
        self.Displacement = Displacement

    def get_data_as_dataframe(self):
        try:
            pass

        except Exception as error:
            logging.info("Exception occured at getting data")
            raise CustomException(error, sys)





