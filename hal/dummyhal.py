from hal.ihal import HAL
from dto.get_dto import GetDto
from dto.set_dto import SetDto


class DummyHAL(HAL):
    def __init__(self, gpio_configuration: dict):
        super().__init__(gpio_configuration)

    def set(self, setparams: SetDto) -> bool:
        print(setparams)
        return True

    def get(self, getparams: GetDto) -> (bool, int):
        print(getparams)
        return True, 1
