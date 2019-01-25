import os


def is_started_by_root() -> bool:
    # Easier to Ask Forgiveness than Permission
    # credits to "msw": https://stackoverflow.com/a/2806932
    try:
        os.rename('/etc/foo', '/etc/bar')
    except IOError:
        return False
    return True


def print_header(description: str='') -> None:
    # Minimum Terminal width required = 80 characters
    print('*'*80)
    print('> SmartNode ~ {description}'.format(description=description))
    print('_'*80)
    print('* '*40)
    print('')
