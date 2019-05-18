import xml.etree.ElementTree as ETree
from .base import Parser


class XmlParser(Parser):
    def __init__(self, path: str):
        tree = ETree.parse(path)
        self._raw = tree.getroot()
