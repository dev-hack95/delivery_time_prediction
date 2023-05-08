import os
import sys
import pickle
sys.path.append("./src")
from logger import logging
from exception import CustomException
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as error:
        raise CustomException(error, sys)
    
def evaulate_model(x_train, x_test, y_train, y_test, models):
        try:
            report = {}
            for i in range(len(models)):
                model = list(models.values())[i]
                model.fit(x_train, y_train)

                #y_train_pred = model.predict(x_train)

                y_test_pred = model.predict(x_test)

                test_model_score = r2_score(y_test, y_test_pred)

                report[list(models.keys())[i]] = test_model_score

            return report

        except Exception as error:
            logging.info("Error occured at evaulating model")
            raise CustomException(error, sys)
        
def load_object(file_path):
     try:
          with open(file_path, 'rb') as file:
               return pickle.load(file_path)
          
     except Exception as error:
          logging.info("Exception occured in load_object function utils")
          raise CustomException(error, sys)