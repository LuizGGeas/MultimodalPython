from Aresta import aresta
from Transportes import Transportes as tr
from Grafo import Grafo
from Caminho import Caminho as c
from Genetico import Genetico as g

arestas = []

arestas.append(aresta(0,1,1,tr(1)))
arestas.append(aresta(0,2,1,tr(2)))
arestas.append(aresta(2,4,9,tr(2)))
arestas.append(aresta(2,9,6,tr(2)))
arestas.append(aresta(4,9,7,tr(2)))
arestas.append(aresta(4,6,7,tr(2)))
arestas.append(aresta(6,23,19,tr(2)))
arestas.append(aresta(6,25,7,tr(2)))
arestas.append(aresta(9,23,15,tr(2)))
arestas.append(aresta(25,23,6,tr(2)))
arestas.append(aresta(23,26,5,tr(2)))
arestas.append(aresta(25,26,10,tr(2)))
arestas.append(aresta(1,3,5,tr(1)))
arestas.append(aresta(1,5,4,tr(1)))
arestas.append(aresta(5,24,4,tr(1)))
arestas.append(aresta(10,24,7,tr(1)))
arestas.append(aresta(24,15,3,tr(1)))
arestas.append(aresta(10,11,7,tr(1)))
arestas.append(aresta(11,15,4,tr(1)))
arestas.append(aresta(15,17,5,tr(1)))
arestas.append(aresta(15,22,7,tr(1)))
arestas.append(aresta(17,20,7,tr(1)))
arestas.append(aresta(17,21,5,tr(1)))
arestas.append(aresta(22,20,7,tr(1)))
arestas.append(aresta(20,21,4,tr(1)))
arestas.append(aresta(21,26,4,tr(1)))
arestas.append(aresta(7,8,5,tr(3)))
arestas.append(aresta(8,12,6,tr(3)))
arestas.append(aresta(12,19,7,tr(3)))
arestas.append(aresta(12,13,20,tr(3)))
arestas.append(aresta(13,16,7,tr(3)))
arestas.append(aresta(16,18,17,tr(3)))
arestas.append(aresta(18,19,7,tr(3)))
arestas.append(aresta(14,19,7,tr(3)))
arestas.append(aresta(19,26,5,tr(3)))
arestas.append(aresta(14,26,8,tr(3)))
arestas.append(aresta(3,7,5,tr(3)))
arestas.append(aresta(7,14,6,tr(4)))
arestas.append(aresta(8,10,17,tr(4)))
arestas.append(aresta(11,13,20,tr(4)))
arestas.append(aresta(21,19,16,tr(4)))

gr = Grafo(27, arestas)

f = open('matrix.txt', 'w')


for i in gr.grafo:
    for j in i:
        f.write(f'{j} ')
    f.write('\n')
f.close()

path = c(grafo = gr.grafo).caminho

gen = g.mutacao(path, gr.grafo)

gen = []

for i in range(100):
    gen.append(c(grafo=gr.grafo))