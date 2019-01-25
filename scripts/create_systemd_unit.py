#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
from sys import argv
from time import time

from envhelper import print_header
from envhelper import is_started_by_root
from locator import get_application_root

_unit_path = '/lib/systemd/system/smartnode.service'
_backup_path = './smartnode_{0}.service.bak'.format(time())
_unit_encoding = 'utf-8'

_unit_file = '''[Unit]
Description=SmartNode
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 {application_root}/webapi.py

[Install]
WantedBy=multi-user.target
'''.format(application_root=get_application_root())


def print_help() -> None:
    print('Script-Usage:')
    print('     create_systemd_unit.py                 runs script as expected')
    print('     create_systemd_unit.py <any params>    displays help-page (this page)')
    print()

    print('Return-Codes:')
    print('     0 - SUCCESS')
    print('     1 - HIGHER PERMISSIONS REQUIRED')
    print('')

    print('Notes:')
    print('     This script must be run as root.')
    print('')

    print('')
    print('')


def read_unit_file() -> str:
    with open(_unit_path, 'r', encoding=_unit_encoding) as fptr:
        return fptr.read()


def create_unit_file() -> None:
    print('Creating Unit-File ...')
    with open(_unit_path, 'w+', encoding=_unit_encoding) as fptr:
        fptr.write(_unit_file)

    print(read_unit_file())
    print('')
    print('CREATED SUCCESSFULLY')


def print_nextsteps():
    print('Next steps:')
    print('     sudo systemctl enable smartnode.service')
    print('     sudo systemctl start smartnode.service')
    print()


if __name__ == '__main__':
    print_header(description='creates a systemd-unit')

    if len(argv) != 1:
        print_help()
        exit(0)

    if not is_started_by_root():
        print('ERROR: This script must be run as root-user (requires root privileges)')
        print('Type "create_systemd_unit.py --help" for further information about this script')
        print('')
        exit(1)

    if os.path.exists(_unit_path):
        print('WARNING: Unit-File does already exist! Creating backup for current unit to "{0}"' + _backup_path)
        print('You can roll-back changes by typing "yes | sudo cp -rf {s} {d}"'.format(s=_backup_path, d=_unit_path))
        with open(_backup_path, 'w+', encoding=_unit_encoding) as backupfile:
            backupfile.write(read_unit_file())

    create_unit_file()
    print_nextsteps()
