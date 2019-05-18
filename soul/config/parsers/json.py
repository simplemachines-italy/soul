from .base import Parser
from json import load


class JsonParser(Parser):
    def __init__(self, path: str):
        stream = open(path, "r")
        self._raw = load(stream)
