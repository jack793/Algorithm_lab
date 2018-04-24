from LibGraph.PIIndirectGraph import PIIndirectGraph

from math import inf

from copy import deepcopy


class PIMapIndirectGraph:
    def __init__(self):
        self._graph = dict()
        self._nodes = dict()

    def get_node_list(self):
        return {(k, v) for k, v in self._nodes.items()}

    def get_arch_list(self):
        return {(k, v) for k, v in self._graph.items()}

    def add_node(self, node, index):
        if node not in self._nodes:
            self._nodes[node] = index
        else:
            if self._nodes[node] is not index:
                raise Exception("Invalid index, already set:", node, index)

    def add_arch(self, node_a, node_b, time):
        i, x, y = node_a
        i2, x2, y2 = node_b
        if x is x2 and y is y2:
            raise Exception("Invalid nodes, can't draw arch from and to the same node.")
        self.add_node((x, y), i)
        self.add_node((x2, y2), i2)
        self._graph[frozenset({node_a, node_b})] = time

    def remove_node(self, node):
        """
        Remove a node from the graph
        :param node: tuple (x,y) containing the coordinates of the node
        :return:
        """
        self._nodes.pop(node)
        for k in self._graph.keys():
            if node in k:
                self._graph.pop(k)

    def remove_arch_by_coord(self, node_a, node_b):
        """
        Remove an arch from the graph by its nodes coordinates
        :param node_a: tuple (x,y) containing the index and the coordinates of the node a
        :param node_b: tuple (x,y) containing the index and the coordinates of the node b
        :return:
        """
        xa, ya = node_a
        xb, yb = node_b
        ia = self._nodes.get(node_a)
        ib = self._nodes.get(node_b)
        self._graph.pop(frozenset({(ia, xa, ya), (ib, xb, yb)}))

    def _remove_arch_by_index(self, ia, ib):
        """
        Remove an arch from the graph by its nodes indexes
        :param ia: index of node a
        :param ib: index of node b
        :return:
        """
        inv_graph = dict({(v, k) for k, v in self._graph.items()})
        xa, ya = inv_graph.get(ia)
        xb, yb = inv_graph.get(ib)
        self._graph.pop(frozenset({(ia, xa, ya), (ib, xb, yb)}))

    def held_karp(self, v, s, d, p):
        """
        :param v: target node
        :param s: lst of nodes we have to go through
        :return:
        """
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

            for u in s1:
                dist = self.held_karp(u, s1, d, pred)  # recursive call
                print("Dist:", dist)

                if dist + self._graph[({u, v})] < min_dist:  # update
                    min_dist = dist + self._graph[frozenset({u, v})]
                    min_prec = u

            d[(v, s)] = min_dist
            pred[(v, s)] = min_prec

            return min_dist
