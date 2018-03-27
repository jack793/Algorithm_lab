# Secondo laboratorio

# 1 - Dopo aver calcolato la resilienza dei tre grafi, mostrate il risultato in un grafico con scala lineare (non
# log/log) che combini le tre curve ottenute. Usate un grafico a punti oppure a linea per ognuna delle curve. L'asse
# orizzontale del grafico deve corrispondere al numero di nodi disattivati dall'attacco (che variano da 0 a n),
# mentre l'asse verticale alla dimensione della componente connessa più grande rimasta dopo aver rimosso un certo
# numero di nodi. Aggiungete una legenda al grafico che permetta di distinguere le tre curve e che specifici i valori
#  di p e m utilizzati. Allegate il file con la figura nell'apposito spazio.
from random import sample

from matplotlib import pyplot as plt
from matplotlib.patches import Patch

from LibGraph.PIIndirectGraph import PIIndirectGraph
from LibGraph.gen.PIGen import PIGen


def gen_real_graph():
    inputFile = open("as19991212.txt", "r")
    for i in range(0, 4):
        inputFile.readline()

    g = PIIndirectGraph()
    for line in inputFile:
        (a, b) = line.split()
        if a != b:
            g.add_arch(a, b)

    return g


m = 2
n = 1476
p = 0.00145290

real_g = gen_real_graph()
er_g = PIGen.gen_indirect_graph_er(n, p)
upa_g = PIGen.gen_indirect_graph_upa(m, n)


def es_random_choice(real_graph, er_graph, upa_graph):
    res_real_graph = [real_graph.get_resilience()]
    res_er_graph = [er_graph.get_resilience()]
    res_upa_graph = [upa_graph.get_resilience()]

    for i in range(len(real_graph.get_node_list())):
        print("I:", i)
        node = sample(real_graph.get_node_list(), 1)[0]
        print("\tn:", node)
        real_graph.remove_node(node)
        res = real_graph.get_resilience()
        print("\tr:", res)
        res_real_graph.append(res)

    for i in range(len(er_graph.get_node_list())):
        print("I:", i)
        node = sample(er_graph.get_node_list(), 1)[0]
        print("\tn:", node)
        er_graph.remove_node(node)
        res = er_graph.get_resilience()
        print("\tr:", res)
        res_er_graph.append(res)

    for i in range(len(upa_graph.get_node_list())):
        print("I:", i)
        node = sample(upa_graph.get_node_list(), 1)[0]
        print("\tn:", node)
        upa_graph.remove_node(node)
        res = upa_graph.get_resilience()
        print("\tr:", res)
        res_upa_graph.append(res)

    plt.suptitle("Resilienza dei grafi")
    plt.title("Scelta casuale")
    plt.legend(handles=[Patch(color='red', label="Real graph"),
                        Patch(color='blue', label="UPA graph (m=2, n=1476)"),
                        Patch(color='green', label="UER graph (n=1476, p=0.00145290)")])
    plt.xlabel("# nodi eliminati")
    plt.ylabel("Dim. componente con. più grande")
    plt.plot(range(len(res_real_graph)), res_real_graph, ".r", markersize=0.5)
    plt.plot(range(len(res_upa_graph)), res_upa_graph, ".b", markersize=0.5)
    plt.plot(range(len(res_er_graph)), res_er_graph, ".g", markersize=0.5)
    plt.show()
    return res_real_graph, res_er_graph, res_upa_graph


def es_greedy_choice(real_graph, er_graph, upa_graph):
    res_real_graph = [real_g.get_resilience()]
    res_er_graph = [er_g.get_resilience()]
    res_upa_graph = [upa_g.get_resilience()]

    node_list = real_graph.get_node_list()
    node_list = sorted(node_list, key=lambda v: len(real_graph.get_adj_list(v)), reverse=True)
    for i in range(len(node_list)):
        node = node_list[i]
        print("I:", i)
        print("\tn:", node)
        print("\ta:", len(real_graph.get_adj_list(node)))
        real_graph.remove_node(node)
        res = real_graph.get_resilience()
        print("\tr:", res)
        res_real_graph.append(res)

    node_list = er_graph.get_node_list()
    node_list = sorted(node_list, key=lambda v: len(er_graph.get_adj_list(v)), reverse=True)
    for i in range(len(node_list)):
        node = node_list[i]
        print("I:", i)
        print("\tn:", node)
        print("\ta:", len(real_graph.get_adj_list(node)))
        er_graph.remove_node(node)
        res = er_graph.get_resilience()
        print("\tr:", res)
        res_er_graph.append(res)

    node_list = upa_graph.get_node_list()
    node_list = sorted(node_list, key=lambda v: len(upa_graph.get_adj_list(v)), reverse=True)
    for i in range(len(node_list)):
        node = node_list[i]
        print("I:", i)
        print("\tn:", node)
        print("\ta:", len(real_graph.get_adj_list(node)))
        upa_graph.remove_node(node)
        res = upa_graph.get_resilience()
        print("\tr:", res)
        res_upa_graph.append(res)

    plt.suptitle("Resilienza dei grafi")
    plt.title("Scelta massima dimensione adiacenza")
    plt.legend(handles=[Patch(color='red', label="Real graph"),
                        Patch(color='blue', label="UPA graph (m=2, n=1476)"),
                        Patch(color='green', label="UER graph (n=1476, p=0.00145290)")])
    plt.xlabel("# nodi eliminati")
    plt.ylabel("Dim. componente con. più grande")
    plt.plot(range(len(res_real_graph)), res_real_graph, ".r", markersize=0.5)
    plt.plot(range(len(res_upa_graph)), res_upa_graph, ".b", markersize=0.5)
    plt.plot(range(len(res_er_graph)), res_er_graph, ".g", markersize=0.5)
    plt.show()

    return res_real_graph, res_er_graph, res_upa_graph


def es_twenty_attack_random(real_graph, er_graph, upa_graph):
    res_real_graph, res_er_graph, res_upa_graph = es_random_choice(real_graph, er_graph, upa_graph)

    print("Resilenza al'80% del grafo reale:", res_real_graph[int(len(res_real_graph) * 0.2)])
    if res_real_graph[int(len(res_real_graph) * 0.2)] > res_real_graph[0] * 0.75:
        print("\tIl grafo reale è resiliente.")
    else:
        print("\tIl grafo reale non è resiliente")
    print("Resilenza al'80% del grafo er:", res_er_graph[int(len(res_er_graph) * 0.2)])
    if res_er_graph[int(len(res_er_graph) * 0.2)] > res_er_graph[0] * 0.75:
        print("\tIl grafo er è resiliente.")
    else:
        print("\tIl grafo er non è resiliente")
    print("Resilenza al'80% del grafo upa:", res_upa_graph[int(len(res_upa_graph) * 0.2)])
    if res_upa_graph[int(len(res_upa_graph) * 0.2)] > res_upa_graph[0] * 0.75:
        print("\tIl grafo upa è resiliente.")
    else:
        print("\tIl grafo upa non è resiliente")


def es_twenty_attack_greedy(real_graph, er_graph, upa_graph):
    res_real_graph, res_er_graph, res_upa_graph = es_greedy_choice(real_graph, er_graph, upa_graph)

    print("Resilenza al'80% del grafo reale:", res_real_graph[int(len(res_real_graph) * 0.2)])
    if res_real_graph[int(len(res_real_graph) * 0.2)] > res_real_graph[0] * 0.75:
        print("\tIl grafo reale è resiliente.")
    else:
        print("\tIl grafo reale non è resiliente")
    print("Resilenza al'80% del grafo er:", res_er_graph[int(len(res_er_graph) * 0.2)])
    if res_er_graph[int(len(res_er_graph) * 0.2)] > res_er_graph[0] * 0.75:
        print("\tIl grafo er è resiliente.")
    else:
        print("\tIl grafo er non è resiliente")
    print("Resilenza al'80% del grafo upa:", res_upa_graph[int(len(res_upa_graph) * 0.2)])
    if res_upa_graph[int(len(res_upa_graph) * 0.2)] > res_upa_graph[0] * 0.75:
        print("\tIl grafo upa è resiliente.")
    else:
        print("\tIl grafo upa non è resiliente")


# es_random_choice(real_g, er_g, upa_g)
es_twenty_attack_random(real_g, er_g, upa_g)
# es_greedy_choice(real_g, er_g, upa_g)
es_twenty_attack_greedy(real_g, er_g, upa_g)
