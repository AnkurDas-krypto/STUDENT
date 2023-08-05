from src.student.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.student.utils.common import read_yaml, create_directories
from src.student.entity import (DataIngestionConfig, 
                                DataValidationConfig,
                                DataTransformationConfig)


class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        create_directories([self.config.artifact_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            train_path = config.train_path,
            test_path= config.test_path,
            raw_path= config.raw_path
        )

        return data_ingestion_config
    
    def get_data_validation(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            validation_status = config.validation_status,
            ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES
        )
        return data_validation_config
    
    def get_data_transformation(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            preprocessor_path = config.preprocessor_path,
            data_path = config.data_path,
            train_arr = config.train_arr,
            test_arr= config.test_arr)
        return data_transformation_config