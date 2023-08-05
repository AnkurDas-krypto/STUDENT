from src.student.config.configuration import ConfigurationManager
from src.student.conponents.data_transformation import DataTransformation
from src.logger import logging
import sys
from src.exception import CustomException


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.initiate_data_transformation()
            logging.info("data transformation successful")
        except Exception as e:
            raise CustomException(e, sys)
