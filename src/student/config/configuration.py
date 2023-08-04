from src.student.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.student.utils.common import read_yaml, create_directories
from src.student.entity import DataIngestionConfig


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