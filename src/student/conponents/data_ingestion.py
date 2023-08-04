import os
import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
import sys
from src.student.config.configuration import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config= DataIngestionConfig):
            self.config = config

    def splitting_data(self):    
        try: 
            df = pd.read_csv("C:/Users/User/Desktop/practice_OOPS/STUDENT/data.csv")

            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

            train_df.to_csv(Path(self.config.train_path) / "train.csv", index=False, header=True)
            test_df.to_csv(Path(self.config.test_path) / "test.csv", index=False, header=True)
            df.to_csv(Path(self.config.raw_path) / "df.csv", index=False, header=True)
            logging.info("splitting successful")
        except Exception as e:
            raise CustomException(e, sys)