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

    def held_karp(self, v, s, d, p):
        """
        :param v: target node
        :param s: lst of nodes we have to go through
        :return:
        """
        # TODO tutte le operazioni vanno fatte su una copia del grafo, NON SULL ORIGINALE! (usare deepcopy)

        # Base case
        if len(s) == 1:  # or == v ?
            print("Base case:", v)
            return self._time[frozenset({v, 0})] # S contiene un unico elemento che è v, stiamo andando da 0 --> v
        elif self._time[frozenset({v, s})] is not None:
            return self._time[frozenset({v, s})]
        else:
            min_dist = float(inf)
            min_prec = None
            S1 = tuple([u for u in s if u != v])
            for u in S1:
                dist = self.held_karp(u, S1)  # recursive call
                print("Dist:", dist)
                # print("currently arch:", self._get_adj_matrix(u, v))
                # print("compare:", dist + self._get_adj_matrix(u, v), min_dist)
                if dist + self._time[({u, v})] < min_dist:  # update
                    min_dist = dist + self._time[frozenset({u, v})]
                    min_prec = u
            self._time[frozenset({v, s})] = min_dist
            self.set_parents((v, s), min_prec)
            return min_dist
