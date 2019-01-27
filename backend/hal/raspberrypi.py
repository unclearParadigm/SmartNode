# from gpiozero import LED

from backend.hal.ihal import HAL


class RaspberryPiHAL(HAL):
    HARDWARE_NAME = 'Raspberry Pi'
    SUPPORTED_INPUT_MODES = ['pwm', 'digital', 'analog']
    SUPPORTED_OUTPUT_MODES = ['pwm', 'digital', 'analog']

    def __init__(self, gpio_configuration: list) -> None:
        super().__init__(gpio_configuration)




