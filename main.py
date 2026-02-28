import logging
from pathlib import Path
from config.logging_config import setup_production_config
from config.config import get_config

from src.orchestrador import Orchestrador

yaml_config_store = Path('./config/logging_config.yaml')
log_file_name = Path('./logs/info.log')

def main():
    logger.info(f"| {' Inicio ':.^120} |")
    config_store = get_config('./config/config.yaml')
    orchestrador = Orchestrador(config_store)
    orchestrador.run()
    logger.info(f"| {' Fin ':.^120} |")


if __name__=='__main__':
    setup_production_config(
        log_file_name=log_file_name
    )
    logger = logging.getLogger(__name__)
    try:
        main()
    except KeyboardInterrupt:
        print()
        logger.info("Proceso interrumpido manualmente")
    except Exception as e:
        logger.error(f"Error: {e}")
        logger.info(f"| {' ERROR ':.^120} |")
