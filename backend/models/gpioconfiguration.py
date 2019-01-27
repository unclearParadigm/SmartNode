class GPIOConfiguration(object):
    def __init__(self, gpio: int, name: str, mode: str, direction: str, inverted: bool=False) -> None:
        self.gpio = int(gpio)  # Number identifying the GPIO
        self.name = str(name)  # Human readable Name, Description
        self.mode = str(mode)  # Digital, Analog, PWM
        self.direction = str(direction)  # Output, Input
        self.inverted = bool(inverted)   # Active High, Active Low
