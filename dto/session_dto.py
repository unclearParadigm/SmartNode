class SessionDto(object):
    def __init__(self, ipv4: str, useragent: str, description: str=None) -> None:
        self.ipv4 = str(ipv4)
        self.useragent = str(useragent)
        self.description = str(description)
