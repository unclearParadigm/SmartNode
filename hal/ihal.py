from dto.get_dto import GetDto
from dto.set_dto import SetDto
from dto.pinconfig_dto import PinConfigDto


class HAL(object):
    HARDWARE_NAME = 'Hardware Abstraction Layer Interface'
    SUPPORTED_INPUT_MODES = []
    SUPPORTED_OUTPUT_MODES = []

    def __init__(self, gpio_configuration: dict) -> None:
        self.gpio_configuration = gpio_configuration

    def configure(self, gpio_configuration: dict) -> None:
        self.gpio_configuration = gpio_configuration

    def reconfigure(self, actor: int, actor_configuration: PinConfigDto) -> None:
        self.gpio_configuration[actor] = actor_configuration

    def set(self, setparams: SetDto) -> bool:
        raise Exception("Cannot call function of interface IHAL - use an implementation instead.")

    def get(self, getparams: GetDto) -> (bool, int):
        raise Exception("Cannot call function of interface IHAL - use an implementation instead.")


