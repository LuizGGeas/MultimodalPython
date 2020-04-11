from Caminho import Caminho
from Grafo import Grafo as gr
import random
class Genetico:

	def selecao(self, caminhos, grafo: gr.grafo):
		todo = []
		if len(caminhos) > 20:
			for i in range(len(caminhos)%5):
				todo.append(random.choice(caminhos))
			
			i1 = todo[random.choice(todo)]
			i2 = i1
			
			while i2 == i1:
				i2 = todo[random.choice(todo)]
			
			n = self.cruzamento(i1, i2, grafo)
			if n not in caminhos:
				caminhos.append(n)

			todo.clear()

			for i in range(len(caminhos)%5):
				todo.append(random.choice(caminhos))
			
			for i in todo:
				self.mutacao(i, grafo)
			
			for i in todo:
				if i not in caminhos:
					caminhos.append(i) 
		
		else:
			caminhos.sort(key= lambda e: e.fitness)
			print(f'melhor elemento de todo o conjunto é: {caminhos[0]}')




	@staticmethod
	def cruzamento(c1:Caminho, c2: Caminho, grafo: gr.grafo):
		aux = [i for i in c1.caminho if i in c2]

		i = random.choice(aux)
		j = i

		while(j == i and aux):
			j = random.choice(aux)
		novo = []
		if len(aux) > 1:
			novo = c1.caminho[0:i]+c2.caminho[i:j]+c1.caminho[j:]
		elif len(aux) == 1:
			novo = c1.caminho[0:i]+ c2.caminho[i:]
		else:
			if c1.fitness >= c2.fitness:
				novo = c2
			else:
				novo = c1
		n = Caminho(grafo, novo)
		return n


	@staticmethod
	def mutacao(c1:Caminho, grafo:gr.grafo):
		print(c1.caminho)
		aux = random.choice(c1.caminho) 
		poss = []
		while not poss:
			poss = [i for i in range(len(grafo)) if grafo[aux][i].value > 0 and i not in c1.caminho]
			if not poss:
				aux = random.choice(c1.caminho)

		i = random.choice(poss)
		c1.caminho[c1.caminho.index(aux)] = i