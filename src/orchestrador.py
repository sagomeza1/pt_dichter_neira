import logging
import logging.config

from typing import Protocol

logger = logging.getLogger(__name__)

class Orchestrador(Protocol):
    
    def get_info_tables(self) -> None:
        pass

    def identify_alerts(self) -> None:
        pass

    def export_audits_report(self) -> None:
        pass
    
    pass

def main():
    pass
if __name__=='__main__':
    main()