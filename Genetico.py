from Caminho import Caminho 
import random
class Genetico:

    @staticmethod
    def mutacao(caminho: Caminho, grafo):
        aux = []
        while not aux:
            aux = [[i for i in caminho if grafo[x][i] > 0] for x in caminho]

        i = random.choice(aux)

        print(i)
        