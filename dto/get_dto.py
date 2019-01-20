class GetDto(object):
    def __init__(self, output: str, actor: int):
        self.output = str(output)
        self.actor = int(actor)

    def __str__(self) -> str:
        return 'GET[{0}-{1}]'.format(str(self.output), str(self.actor))

    def __repr__(self) -> str:
        return self.__str__()
