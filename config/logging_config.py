import sys
import yaml
import logging
import logging.config

from pathlib import Path
from typing import Optional, Callable

logger = logging.getLogger(__name__)
yaml_file_path = Path('logging_config.yaml')

def setup_global_config() -> None:
    """
    Configuración del formato global
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] [%(name)s] - %(message)s',
        stream=sys.stdout
    )
    
def setup_production_config(
        log_file_name: str | None = None,
        yaml_file_path:str | Path = './config/logging_config.yaml'
        ) -> None:
    """Carga la configuración desde YAML"""
    try:
        if not isinstance(yaml_file_path, Path):
            yaml_file_path = Path(yaml_file_path)

        if yaml_file_path and yaml_file_path.exists():
            with open(yaml_file_path, 'r') as yaml_file:
                config_log = yaml.safe_load(yaml_file)

            if log_file_name is not None:
                config_log["handlers"]["file"]["filename"] = log_file_name

            logging.config.dictConfig(config_log)
            logger.info(f"Configuración cargada desde {yaml_file_path.name}")
        else:
            raise FileNotFoundError(f"No se encontro el archivo {yaml_file_path}")
        pass

    except Exception as e:
        logger.error(f"Error inesperado al configurar el logging: {e}")