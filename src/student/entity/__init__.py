
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    train_path: Path
    test_path: Path
    raw_path: Path
