from src.student.config.configuration import ConfigurationManager
from src.student.conponents.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import CustomException
import sys

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.splitting_data()
            logging.info("data ingestion done")
        except Exception as e:
            raise CustomException(e, sys)