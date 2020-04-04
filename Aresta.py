from Transportes import Transportes as tr
class aresta:
    v1 = -1
    v2 = -1
    value = 0
    transp = tr(-1)

    def __init__(self, v1:int, v2:int, value:int, transp:tr):
        self.v1 = v1
        self.v2 = v2
        self.value = value
        self.transp = transp

    def getAresta(self):
        return (self.v1, self.v2, self.value, self.transp)