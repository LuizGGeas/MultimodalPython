import random
from Transportes import Transportes as tr

class Caminho:
    caminho:list = []
    trocas:list = []
    fitness = 0
    numtrocas = 0

    def __init__(self, grafo, caminho:list=[], start:int = 0, end:int = 26):
        if not caminho:
            caminho.append(start)
            i = start
            while(i != end):
                poss = []
                for j in range(len(grafo[i])):
                    if grafo[i][j].value > 0:
                        poss.append(j)
                if poss:
                    i = random.choice(poss)
                    caminho.append(i)
                if i == end:
                    break
        self.caminho = caminho
        self.setFitness(grafo)
        self.setTrocas(grafo)
        
    def setFitness(self, grafo: (int, int)):
        for i in range(len(self.caminho)-1):
            self.fitness += grafo[self.caminho[i]][self.caminho[i+1]].value

    def setTrocas(self, grafo):
        for i in range(len(self.caminho)-1):
            self.trocas.append(grafo[self.caminho[i]][self.caminho[i+1]].transp)
        self.setNumTrocas()

    def setNumTrocas(self):
        for i in range(len(self.trocas)):
            if i+2 < len(self.trocas)-1:
                if self.trocas[i] != tr(4):
                    if self.trocas[i] != self.trocas[i+1]:
                        self.numtrocas+=1
                else:
                    if self.trocas[i-1] == self.trocas[i+1]:
                        self.numtrocas-=1
    
    def validacao(self, grafo:(int, int), end:int) -> bool :
        for i in len(self.caminho)-1:
            if grafo[self.caminho[i]][self.caminho[i+1]][0] <= 0:
                if i > 1 and self.caminho[i] != 26:
                    self.caminho.append(self.caminho.pop(i))
                    i-=1
                if i > 1 and self.caminho[i+1] == end:
                    self.caminho.append(self.caminho.pop(i+1))
                    self.caminho.append(self.caminho.pop(i))
                    i-=2
                if i == 1 and self.caminho[i] == end:
                    return False
        return True