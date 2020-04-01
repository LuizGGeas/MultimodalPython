import random
from Transportes import Transportes as tr
from Grafo import Grafo as gr 

class Caminho:
    caminho:list = []
    trocas:list = []
    fitness = 0
    numtrocas = 0

    def __init__(self, grafo:gr.grafo, caminho:list=[], start:int = 0, end:int = 26):
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
        
    def setFitness(self, grafo: gr.grafo):
        for i in range(len(self.caminho)-1):
            self.fitness += grafo[self.caminho[i]][self.caminho[i+1]].value

    def setTrocas(self, grafo:gr.grafo):
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

    def cruzamento(self, c2: Caminho, grafo: gr.grafo):
        aux = [i for i in self.caminho if i in c2]

        i = random.choice(aux)
        j = i

        while(j == i):
            j = random.choice(aux)
        novo = []
        if len(aux) > 1:
            novo = self.caminho[0:i]+c2.caminho[i:j]+self.caminho[j:]
        elif len(aux) == 1:
            novo = self.caminho[0:i]+ c2.caminho[i:]
        else:
            if self.fitness >= c2.fitness:
                novo = c2
            else:
                novo = self
        n = Caminho(grafo, novo)
        return n

    def mutacao(self, grafo:gr.grafo):
        print(self.caminho)
        aux = random.choice(self.caminho) 
        poss = []
        while not poss:
            poss = [i for i in range(len(grafo)) if grafo[aux][i].value > 0 and i not in self.caminho]
            if not poss:
                aux = random.choice(self.caminho)

        i = random.choice(poss)
        self.caminho[self.caminho.index(aux)] = i
    
    def validacao(self, grafo: gr.grafo, end:int) -> bool :
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