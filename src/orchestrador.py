import logging
import logging.config

from pymongo import MongoClient
from config.config import ConfigStore
from src.getpipelines import PipelineGetter, YAMLPipelineGetter
from src.processrecords import RecordsProcessor, MongoDBProcessor
from src.exporttables import TablesExporter, ExcelExporter
from typing import Protocol

logger = logging.getLogger(__name__)

class Orchestrador(Protocol):

    def __init__(self, config: ConfigStore):
        super().__init__()
        self.config = config
        self.processor, self.exporter = self._begin_helpers()
        logger.debug("Orquestador inicializado.")

    def _begin_helpers(self):
        
        getter = YAMLPipelineGetter(
            yaml_file=self.config.yaml_file_pipeline_getter
        )

        processor = MongoDBProcessor(
            db=self.config.db,
            client=MongoClient(self.config.uri_mongo),
            collections=self.config.collections_to_process,
            pipelines_getter=getter
        )

        exporter = ExcelExporter(
            file_path=self.config.excel_file_to_export,
            db=self.config.db,
            client=MongoClient(self.config.uri_mongo),
            collections=self.config.collections_to_export
        )

        return processor, exporter
    
    def run(self):
        logger.info("Iniciando procesamiento de los registros.")
        self.process_records(self.processor)
        logger.info("Iniciando exportación de los resultados.")
        self.export_summary(self.exporter)
    
    def process_records(self, processor: RecordsProcessor) -> None:
        processor.process()

    def export_summary(self, exporter: TablesExporter) -> None:
        exporter.export()

    def send_report(self, sender) -> None:
        pass
    pass


def main():
    pass
if __name__=='__main__':
    main()