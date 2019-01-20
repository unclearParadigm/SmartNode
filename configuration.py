# Hardware
from hal.ihal import HAL
from hal.raspberrypi import RaspberryPiHAL

# Data Transfer Objects
from dto.person_dto import Person
from dto.pinconfig_dto import PinConfigDto


_VER = '0.0.1'

_PIN = {
    1: PinConfigDto(name='Relais1', output='digital', active_high=True),
    2: PinConfigDto(name='Relais2', output='digital', active_high=True),
    3: PinConfigDto(name='Relais3', output='digital', active_high=True),
    4: PinConfigDto(name='Relais4', output='digital', active_high=True)
}

# Hardware Abstraction Layer, pick the HAL for your device
_HAL = RaspberryPiHAL(_PIN)

# When in Debug-Mode API is launched with the Flask Development Webserver
# This shall be set to true only for development- & testing purposes.
DEBUGMODE = True
DEBUGHOST = 'localhost'
DEBUGPORT = 5000

NODE_LOCATION = 'Bedroom'
NODE_DESCRIPTION = 'Controls lights and fans'
NODE_MAINTAINER = [
    Person('John', 'Doe', 'john.doe@example.com', '1234567890'),
    Person('Jane', 'Doe', 'jane.doe@example.com', '0123456789')
]


def get_pinconfig() -> dict:
    return _PIN


def get_hal() -> HAL:
    return _HAL


def get_version() -> str:
    return _VER
