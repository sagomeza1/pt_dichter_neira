import logging
from pathlib import Path
from config.logging_config import setup_production_config



def main():
    pass

if __name__=='__main__':
    setup_production_config()
    logger = logging.getLogger(__name__)
    main()