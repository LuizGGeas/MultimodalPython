from Content import Content

class Grafo:
    grafo = []

    def __init__(self, tam:int, arestas:list):
        grafo = [[Content()]*tam]*tam
        
        for i in grafo:
            for j in i:
                if i != j:
                    j.value = -1
        
        for i in arestas:
            grafo[i.v1][i.v2].value, grafo[i.v1][i.v2].transp = i.value, i.transp
        
        self.grafo = grafo

    def getGrafo(self):
        return self.grafo