class PinConfigDto(object):
    def __init__(self, name: str, output: str, active_high: bool=True) -> None:
        self.name = str(name)
        self.output = str(output)
        self.active_high = bool(active_high)
