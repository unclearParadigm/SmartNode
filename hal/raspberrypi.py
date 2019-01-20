# from gpiozero import LED

from hal.ihal import HAL
from dto.set_dto import SetDto


class RaspberryPiHAL(HAL):
    def __init__(self, gpio_configuration: dict) -> None:
        super().__init__(gpio_configuration)




