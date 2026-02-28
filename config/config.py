import os
import yaml
import logging

from dotenv import load_dotenv
from pathlib import Path
from typing import Callable
from dataclasses import dataclass

load_dotenv()

uri_mongo = os.getenv('URI', 'mongodb://localhost:27017/')

logger = logging.getLogger(__name__)
yaml_file_path = Path('config.yaml')

@dataclass
class ConfigStore:
    version: 1
    uri_mongo: str
    db: str
    yaml_file_pipeline_getter: str
    collections_to_process: dict[str, str]
    excel_file_to_export: str
    collections_to_export: list[str]
    detalle: str
    obtener_tablas: bool

    def __post_init__(self):
        self.yaml_file_pipeline_getter = self.yaml_file_pipeline_getter if isinstance(self.yaml_file_pipeline_getter, Path) else Path(self.yaml_file_pipeline_getter)
        self.excel_file_to_export = self.excel_file_to_export if isinstance(self.excel_file_to_export, Path) else Path(self.excel_file_to_export)

        self.yaml_file_pipeline_getter.parent.mkdir(parents=True, exist_ok=True)
        self.excel_file_to_export.parent.mkdir(parents=True, exist_ok=True)

def get_config(yaml_file_path: Path = yaml_file_path) -> ConfigStore:
    """Obtiene los parámetros de la configuración"""
    with open(yaml_file_path, 'r') as file:
        config_para = yaml.safe_load(file)
    return ConfigStore(uri_mongo=uri_mongo, **config_para)