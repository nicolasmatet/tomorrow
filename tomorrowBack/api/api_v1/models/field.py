from typing import Union


class Field:
    def __init__(self, attributeName, keyType=None, attributeType=None):
        self.attributeName: str = attributeName
        self.keyType: Union[None, "'HASH'", "'RANGE'"] = keyType
        self.attributeType: Union[None, "'N'", "'S'", "'B'"] = attributeType

