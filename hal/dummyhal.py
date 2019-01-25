import random

from hal.ihal import HAL
from dto.get_dto import GetDto
from dto.set_dto import SetDto


class DummyHAL(HAL):
    HARDWARE_NAME = 'Dummy Device'
    SUPPORTED_INPUT_MODES = ['pwm', 'digital', 'analog', 'i2c']
    SUPPORTED_OUTPUT_MODES = ['pwm', 'digital', 'analog', 'i2c']

    def __init__(self, gpio_configuration: dict) -> None:
        super().__init__(gpio_configuration)

    def set(self, setparams: SetDto) -> bool:
        print(setparams)
        return True

    def get(self, getparams: GetDto) -> (bool, int):
        print(getparams)
        return True, random.choice([0, 1])
