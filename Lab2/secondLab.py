# 1 Dopo aver calcolato la resilienza dei tre grafi, mostrate il risultato in un grafico con scala lineare (non
# log/log) che combini le tre curve ottenute. Usate un grafico a punti oppure a linea per ognuna delle curve. L'asse
# orizzontale del grafico deve corrispondere al numero di nodi disattivati dall'attacco (che variano da 0 a n),
# mentre l'asse verticale alla dimensione della componente connessa più grande rimasta dopo aver rimosso un certo
# numero di nodi. Aggiungete una legenda al grafico che permetta di distinguere le tre curve e che specifici i valori
#  di p e m utilizzati. Allegate il file con la figura nell'apposito spazio.
from random import sample

from LibGraph.gen.PIGen import PIGen

# m = 2
# n = 1476
# p = 0.00145290

m = 2
n = 500
p = 0.05

graph = PIGen.gen_indirect_graph_upa(m, n)

cc = graph.get_connected_components()

resilience_values = [graph.get_resilience()]

for i in range(n):
    print("I:", i)
    node = sample(graph.get_node_list(), 1)[0]
    print("\tnode:", node)
    graph.remove_node(node)
    res = graph.get_resilience()
    print("\tres:", res)
    resilience_values.append(res)
    print("\trvalues:", resilience_values)

print("LEN:", len(resilience_values))
print(resilience_values)
