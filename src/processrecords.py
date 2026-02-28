import logging

from src.getrecords import RecordsGetter
from typing import Protocol
from dataclasses import dataclass
from pymongo import MongoClient
from config.config import get_config

logger = logging.getLogger(__name__)

@dataclass
class Pipeline:
    collection: str
    pipeline: str

class RecordsProcessor(Protocol):

    def process(self) -> None:
        pass

class MongoDBProcessor:

    def __init__(self):
        self.db: str
        self.client = MongoClient
        self.pipelines = list[Pipeline]
