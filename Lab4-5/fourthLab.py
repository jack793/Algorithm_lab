# 1. Algoritmi esatti: implementate l'algoritmo esatto di Held e Karp. Poiché questo algoritmo è di complessità esponenziale, l'implementazione deve interrompere l'esecuzione se non trova la soluzione ottima entro TT minuti, restituendo la soluzione migliore trovata fino a quel momento, se esiste. Molto probabilmente l'algoritmo riuscirà a trovare la soluzione ottima solo per le istanze più piccole (circa 10 nodi), e fornirà una soluzione parziale per quelle più grandi.
# 2. Euristiche costruttive: scegliete una fra le euristiche costruttive viste a lezione ed implementatela: Nearest Neighbour, Closest Insertion, Farthest Insertion, Random Insertion, Cheapest Insertion.
# 3. Algoritmi 2-approssimati: implementate l'algoritmo 2-approssimato basato sull'albero di copertura minimo.

from LibGraph.PIIndirectGraph import PIIndirectGraph

input_file = open("burma14.tsp", "r")
for _ in range(1):
    input_file.readline()

g = PIIndirectGraph()
PI = 3.141592
RRR = 6378.388
nodes = dict()

# VOGLIO LEGGERE LA QUINTA RIGA DEL FILE DI INPUT E CAPIRE SE IL VALORE è GEO O EUC_2D
if ... is "GEO":
    for line in input_file: #Le righe restanti dalla 9 a EOF
    (a, b, c) = line.split()

    # CONVERSIONI
    a = int(a)
    b = float(b)
    c = float(c)

    # LATITUDINE IN RADIANTI
    degb = int(b)
    minb = b - degb
    radb = PI * (degb + 5.0 * minb / 3.0) / 180.0

    # LONGITUDINE IN RADIANTI
    degc = int(c)
    minc = c - degc
    radc = PI * (degc + 5.0 * minc / 3.0) / 180.0

    # INSERIMENTO DI UN NUOVO NODO IN NODES
    nodes[a] = Node(radb, radc)

    # CALCOLO E INSERIMENTO DEGLI ARCHI
    for i in nodes:
        for j in nodes:
            if i is not j: # EVITO DI INSERIRE ARCHI DA UN NODO A SE STESSO
                # MANCANO LE FUNZIONI COS E ACOS CHE PENSO SIANO DEFINITE DIVERSAMENTE IN MATH
                q1 = cos(nodes[i].gety() - nodes[j].gety())
                q2 = cos(nodes[i].getx() - nodes[j].getx())
                q3 = cos(nodes[i].getx() + nodes[j].getx())

                dij = int(RRR * acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0)

                try:
                    g.add_arch(nodes[i], nodes[j], dij) # BISOGNA AGGIUNGERE IL CAMPO PESO(DISTANZA) IN PIINDIRECTGRAPH
                except KeyError:
                    pass


# plt.title("Piano d'Evaquazione")
# plt.xlabel("Capacità totale")
# plt.ylabel("Tempo di percorrenza del Piano")
# plt.plot(cap, times, "b")
# plt.show()

print("FINE")