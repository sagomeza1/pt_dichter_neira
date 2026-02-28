import logging
import numpy as np
import pandas as pd
import datetime as dt
# from config import
from pymongo import MongoClient
from dataclasses import dataclass
from typing import Protocol, TypeAlias

logger = logging.getLogger(__name__)

@dataclass
class FotosRegistro:
    tipo: str
    id: str | None = None
    nombre: str | None = None


@dataclass
class Cliente:
    id: str
    nombre: str
    categorias: list[str]

@dataclass
class Auditoria:
    id: str
    fecha: str | dt.datetime
    auditor: str
    cliente: Cliente
    fotos: FotosRegistro

class RecordsGetter(Protocol):
    
    def get(self) -> list[Auditoria]:
        pass

