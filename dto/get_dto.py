class GetDto(object):
    def __init__(self, mode: str, actor: int) -> None:
        self.mode = str(mode)
        self.actor = int(actor)

    def __str__(self) -> str:
        return 'GET[{0}-{1}]'.format(str(self.mode), str(self.actor))

    def __repr__(self) -> str:
        return self.__str__()
