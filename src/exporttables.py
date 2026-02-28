import logging
import pandas as pd

from pymongo import MongoClient
from typing import Protocol, TypeAlias
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s|%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)

logger = logging.getLogger(__name__)

class TablesExporter(Protocol):
    def export(self) -> None:
        pass

class ExcelExporter:
    def __init__(
            self,
            file_path: str | Path,
            db: str,
            client: MongoClient,
            collections: list[str],
    ):
        self.file_path = file_path if isinstance(file_path, Path) else Path(file_path)
        self.db = db
        self.client = client
        self.collections = collections

    def export(self):
        table_store = self._load_docs()
        with pd.ExcelWriter(self.file_path) as file:
            for sheet, df in table_store.items():
                df.to_excel(file, sheet_name=sheet, index=False)
                logger.debug(f"Hoja {sheet} almacenada.")
                pass
            logger.info(f"Archivo Excel generado: {self.file_path}")
            pass
        pass

    def _load_docs(self) -> dict[str, pd.DataFrame]:
        table_store = dict()
        db = self.client[self.db]
        for collection in self.collections:
            docs = list(db[collection].find())
            # Se genera una tabla y se almacena
            table_store[collection] = pd.DataFrame(docs)
        
        return table_store

def main():
    data_dir_path = Path() / 'data'
    logger.info(f"{data_dir_path.exists()=}")
    data_dir_path.mkdir(parents=True, exist_ok=True)
    logger.info(f"{data_dir_path.exists()=}")
    client = MongoClient("mongodb://localhost:27017/")
    exporter = ExcelExporter(
        file_path=data_dir_path / 'resumen.xlsx',
        db='dyn',
        client=MongoClient("mongodb://localhost:27017/"),
        collections=["cliente", "resumen"]
    )
    exporter.export()

    pass

if __name__=='__main__':
    main()