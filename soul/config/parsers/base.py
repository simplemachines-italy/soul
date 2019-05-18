from abc import ABC
from typing import Union, Type


class Parser(ABC):
    _raw: Union[list, dict] = None

    @property
    def base_type(self) -> Type[Union[list, dict]]:
        if isinstance(self._raw, list):
            return list

        if isinstance(self._raw, dict):
            return dict

    def __getitem__(self, item):
        return self._raw[item]
