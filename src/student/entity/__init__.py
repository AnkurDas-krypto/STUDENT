from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    train_path: Path
    test_path: Path
    raw_path: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    validation_status: Path
    ALL_REQUIRED_FILES: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    preprocessor_path: Path
    data_path: Path
    train_arr: Path
    test_arr: Path  

@dataclass
class ModelTrainerConfig:
    root_dir : Path
    model_path : Path
    train_arr : Path
    test_arr : Path
