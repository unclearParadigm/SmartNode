# from gpiozero import LED

from hal.ihal import HAL
from dto.set_dto import SetDto


class RaspberryPiHAL(HAL):
    HARDWARE_NAME = 'Raspberry Pi'
    SUPPORTED_INPUT_MODES = ['pwm', 'digital', 'analog']
    SUPPORTED_OUTPUT_MODES = ['pwm', 'digital', 'analog']

    def __init__(self, gpio_configuration: dict) -> None:
        super().__init__(gpio_configuration)




