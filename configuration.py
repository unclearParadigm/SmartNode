# -*- coding: utf-8 -*-

# Hardware
from hal.ihal import HAL
from hal.dummyhal import DummyHAL
from hal.raspberrypi import RaspberryPiHAL

# Data Transfer Objects
from dto.person_dto import Person
from dto.pinconfig_dto import PinConfigDto

""" _PIN is a mapping between GPIO-Numbers and their purpose/function. 
For Pin-numbering please refer to a manual of your board"""
_PIN = {
    2: PinConfigDto(name='Bedlamp', mode='digital', kind='output', inverted=True),
    3: PinConfigDto(name='Fan-Control', mode='digital', kind='output', inverted=True),
    4: PinConfigDto(name='Curtains', mode='digital', kind='output', inverted=True),
    14: PinConfigDto(name='Climate', mode='digital', kind='output', inverted=True)
}

NODE_LOCATION = 'Bedroom'
NODE_DESCRIPTION = 'Controls lights and fans'
NODE_MAINTAINER = [
    Person('John', 'Doe', 'john.doe@example.com', '1234567890'),
    Person('Jane', 'Doe', 'jane.doe@example.com', '0123456789')
]


# Hardware Abstraction Layer, pick the HAL for your device
_HAL = DummyHAL(_PIN)


# --------------------------------------------------------------------------------
# NOTE:
# From here on, changes in configuration are not recommended, unless you know what you are doing!
# Please backup your existing configuration before experimenting around here.

# When in Debug-Mode API is launched with the Flask Development Webserver
# This shall be set to true only for development- & testing purposes.
DEBUGMODE = True
DEBUGHOST = 'localhost'
DEBUGPORT = 5000

_VER = '0.0.1'


def get_pinconfig() -> dict:
    return _PIN


def get_hal() -> HAL:
    return _HAL


def get_version() -> str:
    return _VER
