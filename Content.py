from Transportes import Transportes as tr

class Content:
    value: int
    transp:tr

    def __init__(self, value:int=-1, transp:tr =tr(-1)):
        self.transp = transp
        self.value = value
    
    def __str__(self):
        return f'({self.value}, {self.transp})'    