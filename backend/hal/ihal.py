from backend.models.gpiostate import GPIOState
from backend.models.getrequest import GetRequest
from backend.models.setrequest import SetRequest


class HAL(object):
    HARDWARE_NAME = 'Hardware Abstraction Layer Interface'
    SUPPORTED_INPUT_MODES = []
    SUPPORTED_OUTPUT_MODES = []

    def __init__(self, gpio_configuration: list) -> None:
        self.gpio_configuration = gpio_configuration

    def configure(self, gpio_configuration: list) -> None:
        self.gpio_configuration = gpio_configuration

    def set(self, setparams: SetRequest) -> bool:
        raise Exception("Cannot call function of interface IHAL - use an implementation instead.")

    def get(self, getparams: GetRequest) -> (bool, GPIOState):
        raise Exception("Cannot call function of interface IHAL - use an implementation instead.")


