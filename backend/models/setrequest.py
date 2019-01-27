from jsonschema import validate
from jsonschema import ValidationError

from backend.schema.requests import set_schema


class SetRequest(object):
    def __init__(self, validated_instance: dict):
        self.session = str(validated_instance['session'])
        self.mode = str(validated_instance['mode'])
        self.actor = int(validated_instance['actor'])
        self.value = int(validated_instance['value'])

    def __str__(self) -> str:
        return 'SET[{0}-{1}]: {2}'.format(str(self.mode), str(self.actor), str(self.value))

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def create(instance: dict):
        try:
            validate(instance, set_schema)
            return SetRequest(instance)
        except ValidationError:
            return None
