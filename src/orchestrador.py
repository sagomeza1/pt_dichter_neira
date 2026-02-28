import logging
import logging.config

from src.processrecords import RecordsProcessor
from typing import Protocol

logger = logging.getLogger(__name__)

class Orchestrador(Protocol):
    
    def process_records(self, processor: RecordsProcessor) -> None:
        processor.process()

    def identify_alerts(self) -> None:
        pass

    def export_audits_report(self) -> None:
        pass
    
    pass

def main():
    pass
if __name__=='__main__':
    main()