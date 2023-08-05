from src.exception import CustomException
import sys
from src.logger import logging
from src.student.entity import DataValidationConfig
import os

class DataValidation:
    def __init__(self, config = DataValidationConfig):
        self.config = config

    def get_validation_status(self):
        try:
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion"))

            validation_status = True
            for file in self.config.ALL_REQUIRED_FILES:
                if file not in all_files:
                    validation_status = False
                    break

            with open(self.config.validation_status, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            logging.info(f"validation status: {validation_status}")
            return validation_status

        except Exception as e:
            raise CustomException(e, sys)