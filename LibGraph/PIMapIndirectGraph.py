from LibGraph.PIIndirectGraph import PIIndirectGraph

from math import inf

from copy import deepcopy


class PIMapIndirectGraph:
    def __init__(self):
        self._graph = dict()
        self._nodes = set()

    def add_arch(self, node_a, node_b, time):
        self._graph[frozenset({node_a, node_b})] = time
        self._nodes.add(node_a)
        self._nodes.add(node_b)

    def get_arch_list(self):
        return {(k, v) for k, v in self._graph.items()}

    def get_node_list(self):
        return self._nodes

    def remove_arch(self, node_a, node_b):
        self._graph.pop(frozenset({node_a, node_b}))

    def held_karp(self, v:(float,float), s:frozenset(), d:dict(), pred:dict()):

        # TODO tutte le operazioni vanno fatte su una copia del grafo, NON SULL ORIGINALE! (usare deepcopy)

        # Base case
        if len(s) == 1 and s[0] == v:

            print("Base case:", v)
            return self._graph[frozenset({v, list(self.get_node_list())[0]})]
            # S contiene un unico elemento che è v, stiamo andando da 0 --> v

        elif d[v, s] is not None:

            return d[v, s]

        else:
            min_dist = float(inf)
            min_prec = None
            s1 = {u for u in s if u != v}

            for u in S1:
                dist = self.held_karp(u, s1, d, pred)  # recursive call
                print("Dist:", dist)

                if dist + self._graph[({u, v})] < min_dist:  # update
                    min_dist = dist + self._graph[frozenset({u, v})]
                    min_prec = u

            d[(v, s)] = min_dist
            pred[(v, s)] = min_prec

            return min_dist
