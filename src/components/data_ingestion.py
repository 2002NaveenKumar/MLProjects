import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifact","train.csv")
    test_data_path: str = os.path.join("artifact","test.csv")
    raw_data_path: str = os.path.join("artifact","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self): #If data is stored in database, we probably write the code here to fetch it
        logging.info("Entered the data ingestion method")
        try:
            df = pd.read_csv("Notebook\Data\Stud.csv")# reading the dataset
            logging.info("Read the dataset as Dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)         
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)# converted raw data points to csv file            
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)# splitting the data into train and test
            train_set.to_csv(self.ingestion_config.train_data_path, index= False, header= True)# saved the train set
            test_set.to_csv(self.ingestion_config.test_data_path, index= False, header= True)# saved the test set
            logging.info("Ingestion of the data is completed")
            return( self.ingestion_config.train_data_path,self.ingestion_config.test_data_path )
        
        except Exception as e:
            raise CustomException(e,sys)
         
if __name__ =="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()


             
             
