from Content import Content

class Grafo:
    grafo = []

    def __init__(self, tam:int, arestas:list):
        grafo = []
        
        for i in range(tam):
            linha = []
            for j in range(tam):
                if i == j:
                    ob = Content(value=0)
                    linha.append(ob)
                else:
                    ob = Content()
                    linha.append(ob)
            grafo.append(linha)


        for i in arestas:
            grafo[i.v1][i.v2].value, grafo[i.v1][i.v2].transp = i.value, i.transp
            ob = arestas[arestas.index(i)-1] 
            print(i)
            print(ob)
            print(grafo[i.v1][i.v2].value is grafo[ob.v1][ob.v2].value)        
        self.grafo = grafo

    def getGrafo(self):
        for i in self.grafo:
            for j in i:
                print(j, end=" ")
            print()