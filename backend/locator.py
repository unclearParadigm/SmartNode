#!/usr/bin/env python3

import os.path
from pathlib import Path


def get_backend_root() -> str:
    return os.path.dirname(__file__)


def get_frontend_root() -> str:
    return os.path.join(get_root(), 'frontend')


def get_root() -> str:
    return Path(os.path.os.path.dirname(__file__)).parent


if __name__ == '__main__':
    print(get_root())
    print(get_backend_root())
    print(get_frontend_root())
