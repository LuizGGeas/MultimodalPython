from Caminho import Caminho 
from Grafo import Grafo as gr
import random
class Genetico:

    @staticmethod
    def selecao(caminhos, grafo: gr.grafo):
        todo = []
        if len(caminhos > 20):
            for i in range(len(caminhos)%5):
                todo.append(random.choice(caminhos))
            i1 = todo[random.choice(todo)]
            i2 = i1
            while i2 == i1:
                i2 = todo[random.choice(todo)]
            n = i1.cruzamento(i2, grafo)
            caminhos.append(n) if n not in caminhos

			todo.clear()

			for i in range(len(caminhos)%5):
				todo.append(random.choice(caminhos))
			
			for i in todo:
				i.mutacao(grafo)
			for i in todo:
				caminhos.append(i) if i not in caminhos


    