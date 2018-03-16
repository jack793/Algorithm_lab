

import matplotlib.pyplot as plt

from Lab2.UER import gen_indirect_tree
from Lab2.UPA import *

#1
# Dopo aver calcolato la resilienza dei tre grafi, mostrate il risultato in un grafico con scala lineare (non log/log) che combini le tre curve ottenute. Usate un grafico a punti oppure a linea per ognuna delle curve. L'asse orizzontale del grafico deve corrispondere al numero di nodi disattivati dall'attacco (che variano da 0 a n), mentre l'asse verticale alla dimensione della componente connessa più grande rimasta dopo aver rimosso un certo numero di nodi. Aggiungete una legenda al grafico che permetta di distinguere le tre curve e che specifici i valori di p e m utilizzati. Allegate il file con la figura nell'apposito spazio.

m = 2
n = 1476
p = 0.00145290

uer = gen_indirect_tree(n, p)

upa = genUPA(m, n)
