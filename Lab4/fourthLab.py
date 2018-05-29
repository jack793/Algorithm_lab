# 1. Algoritmi esatti: implementate l'algoritmo esatto di Held e Karp. Poiché questo algoritmo è di complessità
# esponenziale, l'implementazione deve interrompere l'esecuzione se non trova la soluzione ottima entro TT minuti,
# restituendo la soluzione migliore trovata fino a quel momento, se esiste. Molto probabilmente l'algoritmo riuscirà
# a trovare la soluzione ottima solo per le istanze più piccole (circa 10 nodi), e fornirà una soluzione parziale per
# quelle più grandi.
# 2. Euristiche costruttive: scegliete una fra le euristiche costruttive viste a lezione ed
# implementatela: Nearest Neighbour, Closest Insertion, Farthest Insertion, Random Insertion, Cheapest Insertion.
# 3. Algoritmi 2-approssimati: implementate l'algoritmo 2-approssimato basato sull'albero di copertura minimo.
from Lab4.algorithms import *
from Lab4.graph import *

geo = False
cont = 1

input_name = "Data/ch150.tsp"

with open(input_name) as f:
    line = f.readline()
    while line != "NODE_COORD_SECTION\n":
        if "EDGE_WEIGHT_TYPE" in line:
            if line.split(":")[1] == " GEO\n":
                geo = True

        line = f.readline()
        cont += 1

dataset = np.loadtxt(input_name, skiprows=cont, comments=["EOF"])

# print(dataset)
# data_length = len(dataset)
# s = tuple(np.arange(data_length))
#
# graph1 = Graph(dataset, geo)
# print("matrix: \n", graph1.get_adj_matrix())
# print(held_karp(graph1, 0, s))

# cheapest_insertion(graph)

graph2 = Graph(dataset, geo)
print(mst_approx(graph2, r=0))
