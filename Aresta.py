import Transportes
class aresta:
    v1:int
    v2:int
    value:int
    transp = 0

    def __init__(self, v1:int, v2:int, value:int, transp:Transportes):
        self.v1 = v1
        self.v2 = v2
        self.value = value
        self.transp = transp

    def getAresta(self):
        return (self.v1, self.v2, self.value, self.transp)