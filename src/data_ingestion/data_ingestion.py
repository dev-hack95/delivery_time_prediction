import os
import sys
import pandas as pd
import haversine as hs
from haversine import Unit
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
sys.path.append("./src")
from logger import logging
from exception import CustomException
#from data_transform import DataTransformation


""" Inititialize the Data Ingestion Configuration """

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('data/raw/', 'train.csv')
    test_data_path:str = os.path.join('data/raw/', 'test.csv')
    raw_data_path:str = os.path.join('data/raw/', 'raw.csv')


class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Method starts")
        try:
            df = pd.read_csv('data/raw/finalTrain.csv')
            logging.info("Dataset read as pandas Dataframe")

            logging.info("Process started of converting Longititude and Latitude into displacement of source and destination")
            
            
            list_1 = []

            def displacement(i):
                 loc1 = (df.loc[i][4], df.loc[i][5])
                 loc2 = (df.loc[i][6], df.loc[i][7])
                 list_1.append(hs.haversine(loc1,loc2, unit=Unit.KILOMETERS))

            for i in range(0, 45584):
                displacement(i)

            df['Displacement'] = pd.DataFrame(list_1)
            logging.info("Process ended of converting Longititude and Latitude into displacement of source and destination")

            

            logging.info("Dropping unecessary data")
            def drop_features(df, feature):
                 df = df.drop([feature], axis=1, inplace=True)
                 return df
            
            drop_features(df, 'ID')
            drop_features(df, 'Delivery_person_ID')
            drop_features(df, 'Restaurant_latitude')
            drop_features(df, 'Restaurant_longitude')
            drop_features(df, 'Delivery_location_latitude')
            drop_features(df, 'Delivery_location_longitude')
            drop_features(df, 'Order_Date')
            drop_features(df, 'Time_Orderd')
            drop_features(df, 'Time_Order_picked')
            

            logging.info(f"Data frame: \n{df.head().to_string()}")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            
            logging.info("Train test split")
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of Data is completed")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as error:
            logging.info("Exception occured at Data Ingestion stage")
            raise CustomException(error, sys)
        

""" Run Data Ingestion """

"""
if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    train_arr, test_arr, _ = DataTransformation().initiate_data_transformation(train_data_path, test_data_path)
"""