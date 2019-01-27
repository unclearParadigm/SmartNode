# -*- coding: utf-8 -*-

# Hardware
from backend.hal.ihal import HAL
from backend.hal.dummyhal import DummyHAL

# Data Transfer Objects
from backend.models.person import Person
from backend.models.gpioconfiguration import GPIOConfiguration

""" _PINCONFIGURATION is a mapping between GPIO-Numbers and their purpose/function. 
For Pin-numbering please refer to a manual of your board"""
_PINCONFIGURATION = [
    GPIOConfiguration(gpio=2, name='Light 1', mode='digital', direction='output', inverted=True),
    GPIOConfiguration(gpio=3, name='Light 2', mode='digital', direction='output', inverted=True),
    GPIOConfiguration(gpio=4, name='Dummy 1', mode='digital', direction='output', inverted=True),
    GPIOConfiguration(gpio=14, name='Switch', mode='digital', direction='output', inverted=True)
]

NODE_LOCATION = 'Bedroom'
NODE_DESCRIPTION = 'Controls lights and fans'
NODE_MAINTAINER = [
    Person('John', 'Doe', 'john.doe@example.com', '1234567890'),
    Person('Jane', 'Doe', 'jane.doe@example.com', '0123456789')
]

# Hardware Abstraction Layer, pick the HAL for your device
_HAL = DummyHAL(_PINCONFIGURATION)


# --------------------------------------------------------------------------------
# NOTE:
# From here on, changes in configuration are not recommended, unless you know what you are doing!
# Please backup your existing configuration before experimenting around here.

# When in Debug-Mode API is launched with the Flask Development Webserver
# This shall be set to true only for development- & testing purposes.
DEBUGMODE = True
DEBUGHOST = 'localhost'
DEBUGPORT = 5000

_BACKEND_VERSION = '0.0.1'


def get_pinconfig() -> list:
    return _PINCONFIGURATION


def get_hal() -> HAL:
    return _HAL


def get_version() -> str:
    return _BACKEND_VERSION
