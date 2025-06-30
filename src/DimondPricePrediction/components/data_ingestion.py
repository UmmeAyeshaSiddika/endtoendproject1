import logging
import os
from datetime import datetime

import pandas as pd
import numpy as np
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import customexception


from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifaces","train.csv")
    test_data_path:str = os.path.join("artifaces","test.csv")
    
                                      

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        
        try:
            data = pd.read_csv(Path(os.path.join("notebook/data","gemstone.csv")))
            logging.info("I have read dataset as a df")
            
            
            os.makedir(os.path.join(self.ingestion_config.raw_data_path),exists = True)
            data.to_csv(self.ingestion_config.raw_data_path,index = False)
            logging.info("I have saved the raw dataset in artifact folder")
            
            logging.info("Here,I have performed train_test_split")
            train_data, test_data = train_test_split(data,test_size=0.25)
            
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("Data ingestion part compled")
        
        
        
        except Exception as e:
            logging.info("exception occured during data ingestion stage")
            raise customexception(e,sys)   