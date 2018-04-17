# 1
# Usate l'algoritmo CCRP per trovare un piano di evacuazione nel grafo della Città di San Francisco.
#
# I nodi sorgente del piano sono i tre ingressi autostradali della città:
#   - nodo 3718987342 (Golden Gate Bridge)
#   - nodo 915248218 (Oakland Bay Bridge)
#   - nodo 65286004 (James Lick Freeway)
#
# I nodi destinazione corrispondono a sei ospedali cittadini:
#   - nodo 261510687 (San Francisco General Hospital)
#   - nodo 3522821903 (UC Medical Center)
#   - nodo 65319958 (Saint Francis Memorial Hospital)
#   - nodo 65325408 (Saint Mary's Medical Center)
#   - nodo 65295403 (CPMP California Campus)
#   - nodo 258913493 (Kaiser-Permanente Medical Center)
#
# Mostrate l'andamento dell'algoritmo in un grafico a linee dove l'asse x corrisponde alle capacità e l'asse y al tempo
# di percorrenza. Il grafico deve mostrare come cresce la capacità ed il tempo di percorrenza al crescere del numero di
# percorsi inseriti nel piano dall'algoritmo.
from math import inf

from matplotlib import pyplot as plt

from LibGraph.PIMapDirectGraph import PIMapDirectGraph

input_file = open("SFroad.txt", "r")
for _ in range(1):
    input_file.readline()

g = PIMapDirectGraph()
speed_limits = [30, 50, 50, 70, 70, 90]
capacity_limits = [500, 750, 1000, 1500, 2000, 4000]

source_nodes = {3718987342, 915248218, 65286004}
destination_nodes = {261510687, 3522821903, 65319958, 65325408, 65295403, 258913493}

i = 1
for line in input_file:
    (a, b, c, d) = line.split()
    a = int(a)
    b = int(b)
    c = float(c)
    d = int(d)
    if a != b:
        try:
            g.add_arch(a, b, c / speed_limits[d - 1], capacity_limits[d - 1])
        except KeyError:
            pass

print("Number of nodes:", len(g.get_node_list()))
print("Number of edges:", len(g.get_arch_list()))

plan = g.ccrp(source_nodes, destination_nodes)
print(plan)
print("Number of paths:", len(plan))

# Calculate total capacity of the plan
plan_capacity = sum(c for p, c, t in plan)

# Calculate travel time of the plan
_, _, plan_time = plan[-1]

print("Plan capacity:", plan_capacity)
print("Plan time:", plan_time)

capacities = [0]
for p, c, t in plan:
    capacities.append(c + capacities[-1])
capacities = capacities[1:]

plt.title("Piano d'Evaquazione")
plt.xlabel("Capacità totale")
plt.ylabel("Tempo di percorrenza del Piano")
plt.plot(capacities, [t for p, c, t in plan], "b")
plt.show()

# 2 Qual'è la capacità massima di veicoli che possono entrare in città dai tre nodi sorgente? Qual'è la capacità
# massima di veicoli che possono giungere contemporaneamente ai sei ospedali di destinazione? Confrontate questi due
# valori con la capacità massima del piano che avete trovato con CCRP: dove si trova il collo di bottiglia?
print("Source nodes capacity", sum(g.get_capacity(a, b) for a in source_nodes for b in g.get_out_adj_list(a)))
print("Destination nodes capacity",
      sum(g.get_capacity(a, b) for b in destination_nodes for a in g.get_in_adj_list(b)))

bottlenecks = list()
for p, c, t in plan:
    bot = inf
    global res
    for i in range(len(p) - 1):
        if bot > g.get_capacity(p[i], p[i + 1]):
            bot = g.get_capacity(p[i], p[i + 1])
            res = (p[i], p[i + 1])
    bottlenecks.append((res, bot))

print("Bottlenecks:", bottlenecks)

# 3
#
# Spiegate brevemente come avete implementato la coda di priorità nell'algoritmo di Dijkstra per la ricerca dei
# cammini minimi. Qual'è la complessità delle operazioni di base della vostra implementazione: creazione della coda,
# estrazione del minimo e decremento della chiave?



print("FINE")
