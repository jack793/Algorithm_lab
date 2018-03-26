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


# 2
# Qual'è la capacità massima di veicoli che possono entrare in città dai tre nodi sorgente? Qual'è la capacità
# massima di veicoli che possono giungere contemporaneamente ai sei ospedali di destinazione? Confrontate questi due
# valori con la capacità massima del piano che avete trovato con CCRP: dove si trova il collo di bottiglia?


# 3
#
# Spiegate brevemente come avete implementato la coda di priorità nell'algoritmo di Dijkstra per la ricerca dei
# cammini minimi. Qual'è la complessità delle operazioni di base della vostra implementazione: creazione della coda,
# estrazione del minimo e decremento della chiave? 