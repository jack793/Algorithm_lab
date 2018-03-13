# 1
# Questa domanda richiede di analizzare il grafo delle citazioni di 27770 articoli di fisica delle alte energie.
# Il grafo ha 352807 archi ed è contenuto nel file allegato. Ogni articolo del dataset è identificato da un numero.
# Ogni riga del file contiene un arco del grafo dove il primo numero è la coda ed il secondo la testa dell'arco. Il
# compito da svolgere per questa domanda è di calcolare la distribuzione del grado entrante del grafo delle
# citazioni. La distribuzione deve essere normalizzata (i valori devono sommare a 1). Il risultato deve essere
# mostrato in un grafico di dispersione (o plot) dei punti con doppia scala logaritmica (log-log plot). Il file con
# l'immagine del grafico va caricata nell'apposito spazio che compare dopo aver premuto sul bottone "Aggiungi
# consegna".


import matplotlib.pyplot as plt

from Lab1.ER import gen_direct_tree
from Lab1.DPA import *

print("Esercizio 1\n")

# inputFile = open("test_input.txt", "r")

inputFile = open("cit-HepTh.txt", "r")
for i in range(0, 4):
    inputFile.readline()

nodes_grades = dict()
for line in inputFile:
    (a, b) = line.split()
    if a not in nodes_grades:
        nodes_grades[a] = 0
    if b not in nodes_grades:
        nodes_grades[b] = 0
    nodes_grades[b] += 1

print("Nodes:", nodes_grades)

grades_occurrences = dict()
for node in nodes_grades:
    if nodes_grades[node] not in grades_occurrences:
        grades_occurrences[nodes_grades[node]] = 0
    grades_occurrences[nodes_grades[node]] += 1

print("Grades:", grades_occurrences)

grades_distribution = {k: v / len(nodes_grades) for k, v in grades_occurrences.items()}

print("Grades distribution:", grades_distribution)
plt.title("Linear scale")
plt.plot(grades_distribution.keys(), grades_distribution.values(), "go")
plt.show()
plt.title("Log log scale")
plt.loglog(grades_distribution.keys(), grades_distribution.values(), "go")
plt.show()

# 2
# A lezione abbiamo visto l'algoritmo ER(n, p) per generare grafi casuali. Confrontate la forma della distribuzione
# che avete ottenuto nella Domanda 1 con quella generata da ER. Per farlo potete generare diversi grafi casuali per
# valori diversi di n e di p. Rispondete quindi alle seguenti domande:
#  - Com'è fatta la distribuzione del grado entrate di un grafo generato con ER? Descrivete a parole la sua forma.
#  - Ha una forma simile a quella del grafo delle citazioni oppure no? Spiegate brevemente le differenze e le
#    somiglianze tra le due distribuzioni.
# Inserite le risposte nella casella di testo che appare dopo aver premuto sul bottone "Aggiungi consegna"

print("\nEsercizio 2\n")

r_graph = gen_direct_tree(2000, 0.1)
print("Graph:", r_graph)

r_nodes_grades = dict()
for out_node in r_graph:
    for in_node in r_graph[out_node]:
        if in_node not in r_nodes_grades:
            r_nodes_grades[in_node] = 0
        r_nodes_grades[in_node] += 1

print("Nodes grades:", r_nodes_grades)

r_grades_occurrences = dict()
for node in r_nodes_grades:
    if r_nodes_grades[node] not in r_grades_occurrences:
        r_grades_occurrences[r_nodes_grades[node]] = 0
    r_grades_occurrences[r_nodes_grades[node]] += 1

print("Grades occurrences:", r_grades_occurrences)

r_grades_distribution = {k: v / len(r_nodes_grades) for k, v in r_grades_occurrences.items()}

print("Grades distribution:", r_grades_distribution)

plt.title("Linear scale")
plt.plot(r_grades_distribution.keys(), r_grades_distribution.values(), "ro")
plt.show()
plt.title("Log log scale")
plt.loglog(r_grades_distribution.keys(), r_grades_distribution.values(), "ro")
plt.show()

# 3
# Considerate ora l'Algoritmo DPA(m, n) per generare grafi casuali visto a lezione.
# Implementate l'algoritmo e usatelo per generare un grafo casuale con un numero di nodi
# e di archi simile al grafo delle citazioni. Scegliere il valore n da passare all'algoritmo è facile:
# basta usare un valore vicino al numero di nodi del grafo delle citazioni. Siccome ogni iterazione dell'algoritmo
# aggiunge m archi al grafo, usare un valore intero vicino al grado uscente medio del grafo delle citazioni
# è una buona scelta per m.
#
# Dopo aver scelto m e n, generate il grafo casuale e calcolate la distribuzione del grado entrate normalizzata.
# Specificare i valori di m e n che avete scelto nella casella di testo che appare dopo aver premuto sul bottone
# "Aggiungi consegna" e allegate il file con il grafico di dispersione in scala log-log come nella Domanda 1.

print("\nEsercizio 3\n")

dpa = DPATrial(10)

dpa_nodes, dpa_graph = gen(1, 100)

dpa_nodes_grades = dict()
for a, b in dpa_graph:
    if a not in dpa_nodes_grades:
        dpa_nodes_grades[a] = 0
    if b not in dpa_nodes_grades:
        dpa_nodes_grades[b] = 0
    dpa_nodes_grades[b] += 1

dpa_grades_occurrences = dict()
for g in dpa_nodes_grades.values():
    if g not in dpa_grades_occurrences:
        dpa_grades_occurrences[g] = 0
    dpa_grades_occurrences[g] += 1

dpa_grades_distribution = {k: v / len(dpa_nodes) for k, v in dpa_grades_occurrences.items()}

plt.title("Linear scale")
plt.plot(dpa_grades_distribution.keys(), dpa_grades_distribution.values(), "bo")
plt.show()
plt.title("Log log scale")
plt.loglog(dpa_grades_distribution.keys(), dpa_grades_distribution.values(), "bo")
plt.show()



#4
# Confrontate le distribuzioni del grado entrate che avete ottenuto per la Domanda 1 e per la Domanda 4.
# Considerate le somiglianze e le differenze tra le distribuzioni e quali potrebbero essere le cause delle
# somiglianze. Per aiutarvi nell'analisi considerate i seguenti fenomeni:
# - Il fenomeno dei "sei gradi di separazione"
# - Il fenomeno "rich get richer"
# - Il fenomeno della "struttura gerarchica delle reti"
#
# Considerate come questi fenomeni possono spiegare i risultati che avete ottenuto rispondendo alle
# seguenti domande nella casella di testo che appare dopo aver premuto sul bottone "Aggiungi consegna"
#
# - La distribuzione del grafo delle citazioni assimiglia a quella del grafo ottenuto con DPA?
#   Spiegate brevemente similitudini e differenze.
# - Quale dei tre fenomeni spiega meglio il comportamento dell'algoritmo DPA? Spiegate brevemente perché.
# - Quale dei tre fenomeni spiega meglio la struttura del grafo delle citazioni? Spiegate brevemente perché.

# The phenomenon “rich gets richer” mimics the behaviour of the DPA process. When more nodes join the graph network,
# with higher probability they select among a few of nodes as the neighbours that are already rich (i.e., they already
#  have high in-degrees), thereby increasing their in-degrees again. The majority of the nodes that have low in-degrees
#   they tend not to get selected as neighbours with high probability in this process, hence their in-degrees do not 
#   increase. This process modeled by the algorithm DPA mimics the rich gets richer model, but is also used to explain 
#   the six degrees of separation phenomenon.

# Same phenomenon “rich gets richer” can explain the citation graph network structure as well. Few of the papers that 
# are heavily cited (rich, with high in-degrees) becomes an important paper and tend to get cited again with high 
# probability, when a new paper is written it cites those few heavily cited papers again thereby increasing the in-degree
#  of them (making them richer) and it cites the majority of papers with low citations (low importance) with low 
#  probability, so they are likely to remain not cited again.

