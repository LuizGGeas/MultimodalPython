import Aresta

class Grafo:
    grafo = []

    def __init__(self, tam:int, arestas:Aresta):
        grafo = [[(0,0)]*tam]*tam
        
        for i in grafo:
            for j in i:
                if i != j:
                    j = (-1, -1)
        
        for i in arestas:
            grafo[i[0]][i[1]] = (i[2], i[3])
        
        self.matriz = grafo

    def getGrafo(self):
        return self.grafo