import logging

from typing import Protocol
from pymongo import MongoClient
from src.getpipelines import PipelineGetter


logger = logging.getLogger(__name__)

class RecordsProcessor(Protocol):
    def process(self) -> None:
        pass

class MongoDBProcessor:

    def __init__(
            self,
            db: str,
            client: MongoClient,
            collections: dict[str, str],
            pipelines_getter: PipelineGetter
            ):
        self.db = db
        self.client = client
        self.collections = collections
        self.pipelines_getter = pipelines_getter

    def process(self):
        db = self.client[self.db]

        for collection , base_collection in self.collections.items():
            pipeline = self.pipelines_getter.get(collection)
            logger.debug(f"{pipeline=}")
            docs = list(db[base_collection].aggregate(pipeline))
            logger.info(f"Registros obtenidos: {len(docs)}")

            db[collection].drop()
            logger.debug(f"Se limpia la colección {collection}.")
            db[collection].insert_many(docs)
            logger.info(f"Se guardan {len(docs)} docs en {self.db}.{collection}")
            

def main():
    from pathlib import Path
    from src.getpipelines import YAMLPipelineGetter
    
    yaml_file = Path().cwd() / "config" / "pipelines.yaml"
    logger.info(f"{yaml_file.exists()}")

    client = MongoClient("mongodb://localhost:27017/")
    MongoDBProcessor(
        "dyn",
        client,
        {
            # info collections
            "cliente": "registro",
            "auditoria": "registro",
            "categoria": "registro",
            "cliente_auditoria": "registro",
            "cliente_categoria": "registro",
            "auditoria_categoria": "registro",
            "foto_cargada": "registro",
            # agg collections
            "fotos_requeridas_por_cliente": "cliente_categoria",
            "fotos_registradas_por_auditoria": "foto_cargada",
            "resumen": "fotos_registradas_por_auditoria",
        },
        YAMLPipelineGetter(yaml_file)
        ).process()


if __name__=='__main__':
    main()
