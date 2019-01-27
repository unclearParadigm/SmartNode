class GetRequest(object):
    def __init__(self, gpio: int) -> None:
        self.gpio = int(gpio)

    def __str__(self) -> str:
        return 'GET[{0}]'.format(str(self.gpio))

    def __repr__(self) -> str:
        return self.__str__()
