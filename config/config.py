import sys
import yaml
import logging
import logging.config

from pathlib import Path
from typing import Callable
from dataclasses import dataclass

logger = logging.getLogger(__name__)
yaml_file_path = Path('config.yaml')

@dataclass
class Config:
    version: 1
    detalle: str
    obtener_tablas: bool
    uri_mongo: str

def get_config(yaml_file_path: Path = yaml_file_path) -> Config:
    """Obtiene los parámetros de la configuración"""


    if yaml_file_path and yaml_file_path.exists():
        with open(yaml_file_path, 'r') as yaml_file:
            config_log = yaml.safe_load(yaml_file)

    pass