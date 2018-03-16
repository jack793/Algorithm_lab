import random


class UPATrial:
    _numNodes = 0
    _nodeNumbers = []

    # Costruttore
    def __init__(self, num_nodes):
        self._numNodes = num_nodes
        self._nodeNumbers = [node for node in range(num_nodes)
                             for _ in range(num_nodes)]

    def run_trial(self, num_nodes):
        cont = 0
        new_neighbours = set()
        for _ in range(num_nodes):
            v = random.choice(self._nodeNumbers)
            if v not in new_neighbours:
                cont += 1
                new_neighbours.add(v)

        for _ in range(0, cont):
            self._nodeNumbers.append(self._numNodes)

        self._nodeNumbers.extend(list(new_neighbours))
        self._numNodes += 1

        return new_neighbours


def gen(m,n):
    """
    DPA algorithm to generate random graphs
    :param m: number of nodes
    :param n: number 1 <= m <= n
    """
    graph_nodes = set(range(0, m))
    graph = [(a, b) for a in graph_nodes for b in graph_nodes if a != b]
    trial = UPATrial(m)
    for u in range(m, n):
        new_graph_nodes = trial.run_trial(m)
        graph_nodes.add(u)
        for v in new_graph_nodes:
            graph.append((u, v))
            graph.append((v, u))
    return graph_nodes, graph
