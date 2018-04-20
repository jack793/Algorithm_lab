from LibGraph.PIIndirectGraph import PIIndirectGraph

from copy import deepcopy


class PIMapIndirectGraph:
    def __init__(self):
        self._time = dict()
        self._graph = PIIndirectGraph()
        self._parents = {}

    def add_arch(self, node_a, node_b, time):
        self._graph.add_arch(node_a, node_b)
        self._time[frozenset({node_a, node_b})] = time
        # TODO parents

    def get_arch_list(self):
        arch_list = self._graph.get_arch_list()
        return frozenset({(a, b, self._time[frozenset({a, b})]) for a, b in arch_list})
        # TODO parents

    def remove_arch(self, node_a, node_b):
        self._graph.remove_arch(node_a, node_b)
        self._time.pop(frozenset({node_a, node_b}))
        # TODO parents

    def get_parents(self, key):
        return self._parents[key]

    def set_parents(self, key, value):
        self._parents[key] = value

    def held_karp(self, v, s):
        """
        :param v: target node
        :param s: lst of nodes we have to go through
        :return:
        """
        # TODO tutte le operazioni vanno fatte su una copia del grafo, NON SULL ORIGINALE! (usare deepcopy)

        # Base case
        if len(s) == 1: # or == v ?
            print("Base case:", v)
            return self._time[({v, 0})] # S contiene un unico elemento che è v, stiamo andando da 0 --> v
        elif self._time[({v, s})] is not None:
            return self._time[({v, s})]
        else:
            min_dist = float('inf')
            min_prec = None
            S1 = tuple([u for u in s if u != v])
            for u in S1:
                dist = self.held_karp(u, S1)  # recursive call
                print("Dist:", dist)
                print("currently arch:", graph.get_adj_matrix(u, v))
                print("compare:", dist + graph.get_adj_matrix(u, v), min_dist)
                if dist + self._time[({u, v})] < min_dist:  # update
                    min_dist = dist + self._time[({u, v})]
                    min_prec = u
            self._time[({v, s})] = min_dist
            self.set_parents((v, s), min_prec)
            return min_dist
