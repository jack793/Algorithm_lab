

import matplotlib.pyplot as plt

from Lab2.UER import gen_indirect_tree
import LibGraph.gen.PIGen
from LibGraph.PIIndirectGraph import *

# 1 Dopo aver calcolato la resilienza dei tre grafi, mostrate il risultato in un grafico con scala lineare (non
# log/log) che combini le tre curve ottenute. Usate un grafico a punti oppure a linea per ognuna delle curve. L'asse
# orizzontale del grafico deve corrispondere al numero di nodi disattivati dall'attacco (che variano da 0 a n),
# mentre l'asse verticale alla dimensione della componente connessa più grande rimasta dopo aver rimosso un certo
# numero di nodi. Aggiungete una legenda al grafico che permetta di distinguere le tre curve e che specifici i valori
#  di p e m utilizzati. Allegate il file con la figura nell'apposito spazio.

from LibGraph.gen.PIGen import *
m = 2
n = 1476
p = 0.00145290

uer = gen_indirect_tree(n, p)

graph = PIGen.gen_indirect_graph_upa(m, n)

print(graph.get_arch_list())

cc = graph.undirected_connected_components()

#attack_list =

def calc_resilience(ugraph, attack_list):
    '''

    Calculate graph resilience (size of the largest connected component)
    after removing each nodes.

    '''
    #ugraph = alg_application2_provided.copy_graph(ugraph)
    resilience = [PIIndirectGraph.undirected_connected_components()]
    for node in attack_list:
        graph.remove_node(node)
        resilience.append(graph.undirected_connected_components())
    return resilience
