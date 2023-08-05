from src.student.config.configuration import ConfigurationManager
from src.student.conponents.data_validation import DataValidation
from src.logger import logging
from src.exception import CustomException
import sys

class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation()
            data_validation = DataValidation(data_validation_config)
            data_validation.get_validation_status()
            logging.info("data validation successful")
        except Exception as e:
            raise CustomException(e, sys)
    