from src.student.config.configuration import ConfigurationManager
from src.logger import logging
import sys
from src.exception import CustomException
from src.student.conponents.model_trainer import ModelTrainer


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer()
            model_trainer = ModelTrainer(model_trainer_config)
            score = model_trainer.initiate_model_trainer()
            logging.info(f"score is {score}")
        except Exception as e:
            raise CustomException(e, sys)