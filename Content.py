from Transportes import Transportes as tr

class Content:
    value: int
    transp:tr

    def __init__(self, value:int=0, transp:tr = None):
        self.transp = transp
        self.value = value
    def __str__(self):
        return f'({self.value}, {self.transp})'    