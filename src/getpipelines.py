import logging
import yaml
from typing import Protocol
from pathlib import Path

logger = logging.getLogger(__name__)

class PipelineGetter(Protocol):

    def get(self, collection: str) -> dict[str, str]:
        pass

class YAMLPipelineGetter:
    def __init__(self, yaml_file):
        self.yaml_file: str | Path = yaml_file

    def get(self, collection:str) -> dict[str, str]:
        pipelines = self._read_yaml()
        return pipelines[collection]

    def _read_yaml(self):
        with open(self.yaml_file) as file:
            pipelines = yaml.safe_load(file)
        return pipelines
    
def main():
    yaml_file = Path().cwd() / "config" / "pipelines.yaml"
    logger.info(f"{yaml_file.exists()}")
    pipeline = YAMLPipelineGetter(yaml_file).get('clientes')
    logger.info(f"{pipeline=}")

if __name__=='__main__':
    main()
