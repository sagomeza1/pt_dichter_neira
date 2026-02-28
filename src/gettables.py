import pandas as pd
import numpy as np
from config.config import get_config
from typing import Protocol

from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)

class TablesGetter(Protocol):

    def __init__(self):
        super().__init__()
        

    def get(self) -> None:
        pass