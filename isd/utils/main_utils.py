import os.path
import sys
import yaml
import base64

from isd.exception import isdException
from isd.logger import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise isdException(e, sys) from e