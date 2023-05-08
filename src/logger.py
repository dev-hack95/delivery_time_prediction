import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) 
os.makedirs(logs_path, exist_ok=True) # Creating logs file

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


""" The Code attempts to log the time and line number"""
""" 
The Format of the log is [ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s
where % represent a placeholder for an empty string and () represents place holder for arguments passed into function
"""
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

