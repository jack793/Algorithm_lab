# 1
# Usate l'algoritmo CCRP per trovare un piano di evacuazione nel grafo della Città di San Francisco. I nodi
# sorgente del piano sono i tre ingressi autostradali della città:
#
# nodo 3718987342 (Golden Gate Bridge) nodo 915248218 (Oakland Bay Bridge) nodo 65286004 (James Lick Freeway) I nodi
# destinazione corrispondono a sei ospedali cittadini: nodo 261510687 (San Francisco General Hospital) nodo
# 3522821903 (UC Medical Center) nodo 65319958 (Saint Francis Memorial Hospital) nodo 65325408 (Saint Mary's Medical
# Center) nodo 65295403 (CPMP California Campus) nodo 258913493 (Kaiser-Permanente Medical Center) Mostrate
# l'andamento dell'algoritmo in un grafico a linee dove l'asse x corrisponde alle capacità e l'asse y al tempo di
# percorrenza. Il grafico deve mostrare come cresce la capacità ed il tempo di percorrenza al crescere del numero di
# percorsi inseriti nel piano dall'algoritmo.
from matplotlib import pyplot as plt

from LibGraph.PIMapDirectGraph import PIMapDirectGraph

input_file = open("SFroad.txt", "r")
for _ in range(1):
    input_file.readline()

g = PIMapDirectGraph()
speed_limits = [30, 50, 50, 70, 70, 90]
capacity_limits = [500, 750, 1000, 1500, 2000, 4000]

for line in input_file:
    (a, b, c, d) = line.split()
    if a != b:
        try:
            g.add_arch(int(a), int(b), float(c) / speed_limits[int(d) - 1], capacity_limits[int(d) - 1])
        except KeyError:
            pass

plan, capacities, times = g.ccrp({3718987342, 915248218, 65286004},
                                 {261510687, 3522821903, 65319958, 65325408, 65295403, 258913493})

print(plan, capacities, times)

cap = capacities

for i in range(1, len(cap)):
    cap[i] += cap[i - 1]

plt.title("Piano d'Evaquazione")
plt.xlabel("Capacità totale")
plt.ylabel("Tempo di percorrenza del Piano")
plt.plot(cap, times, "b")
plt.show()

print("FINE")

# 2
# Qual'è la capacità massima di veicoli che possono entrare in città dai tre nodi sorgente? Qual'è la capacità
# massima di veicoli che possono giungere contemporaneamente ai sei ospedali di destinazione? Confrontate questi due
# valori con la capacità massima del piano che avete trovato con CCRP: dove si trova il collo di bottiglia?


# 3
#
# Spiegate brevemente come avete implementato la coda di priorità nell'algoritmo di Dijkstra per la ricerca dei
# cammini minimi. Qual'è la complessità delle operazioni di base della vostra implementazione: creazione della coda,
# estrazione del minimo e decremento della chiave?
