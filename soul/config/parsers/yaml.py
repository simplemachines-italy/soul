from yaml import safe_load
from .base import Parser


class YamlParser(Parser):
    def __init__(self, path: str):
        stream = open(path, "r")
        self._raw = safe_load(stream)
