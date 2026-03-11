import os
import sys
import pickle
import pandas as pd
import numpy as np  
from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        logging.info('Saving object to file')
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
        logging.info('Object saved successfully')
    except Exception as e:
        raise CustomException(e, sys)