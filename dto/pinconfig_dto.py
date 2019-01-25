class PinConfigDto(object):
    def __init__(self, name: str, mode: str, kind: str, inverted: bool=False) -> None:
        self.name = str(name)  # Human readable Name
        self.mode = str(mode)  # Digital, Analog, PWM
        self.kind = str(kind)  # Output, Input
        self.inverted = bool(inverted)
