class GPIOState(object):
    def __init__(self, gpio: int, high: bool, low: bool, timestamp: int):
        self.gpio = int(gpio)
        self.high = bool(high)
        self.log = bool(low)
        self.timestamp = int(timestamp)
