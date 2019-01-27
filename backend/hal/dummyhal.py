import time
import random

from backend.hal.ihal import HAL
from backend.models.gpiostate import GPIOState
from backend.models.getrequest import GetRequest
from backend.models.setrequest import SetRequest


class DummyHAL(HAL):
    HARDWARE_NAME = 'Dummy Device'
    SUPPORTED_INPUT_MODES = ['pwm', 'digital', 'analog', 'i2c']
    SUPPORTED_OUTPUT_MODES = ['pwm', 'digital', 'analog', 'i2c']

    def __init__(self, gpio_configuration: list) -> None:
        super().__init__(gpio_configuration)

    def set(self, setparams: SetRequest) -> bool:
        print(setparams)
        return True

    def get(self, getparams: GetRequest) -> (bool, GPIOState):
        print(getparams)
        value = random.choice([0, 1])
        response = GPIOState(gpio=getparams.gpio, high=value, low=not value, timestamp=int(time.time()))
        return True, response
