#!/usr/bin/env python3

import os.path


def get_application_root() -> str:
    return os.path.dirname(__file__)


if __name__ == '__main__':
    print(get_application_root())
