from .field import Field
from .model import Model


class Question(Model):
    id = Field('id', keyType='HASH', attributeType='N')
    title = Field('title')
    type = Field('type')
    choices = Field('choices')

    class Meta:
        readCapacityUnits = 10
        writeCapacityUnits = 10
