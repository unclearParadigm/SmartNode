from jsonschema import validate
from jsonschema import ValidationError

from schema.requests import set_schema


class SetDto(object):
    def __init__(self, validated_instance: dict):
        self.auth = str(validated_instance['auth'])
        self.output = str(validated_instance['output'])
        self.actor = int(validated_instance['actor'])
        self.value = int(validated_instance['value'])

    def __str__(self) -> str:
        return 'SET[{0}-{1}]: {2}'.format(str(self.output), str(self.actor), str(self.value))

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def create(instance: dict):
        try:
            validate(instance, set_schema)
            return SetDto(instance)
        except ValidationError:
            return None
