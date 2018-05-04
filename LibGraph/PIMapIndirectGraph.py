from math import inf


class PIMapIndirectGraph:
    def __init__(self):
        self._graph = dict()
        self._nodes = dict()

    def get_node_list(self):
        return {(k, v) for k, v in self._nodes.items()}

    def get_arch_list(self):
        return {(k, v) for k, v in self._graph.items()}

    def get_node_id_by_coord(self, x, y):
        return self._nodes[(x, y)]

    def get_node_coord_by_id(self, node_id):
        for k, v in self._nodes.items():
            if v is node_id:
                return k
        raise KeyError("Invalid id")

    def add_node(self, x, y, index):
        if (x, y) not in self._nodes.keys() and index not in self._nodes.values():
            self._nodes[(x, y)] = index
        else:
            try:
                if self._nodes[(x, y)] is not index:
                    raise Exception("Invalid coordinates, already set:", (x, y), index)

            except KeyError:
                raise Exception("Invalid index, already set:", (x, y), index)

    def add_arch(self, node_a, node_b, time):
        x, y, i = node_a
        x2, y2, i2 = node_b
        if x is x2 and y is y2:
            raise Exception("Invalid nodes, can't draw arch from and to the same node.")
        self.add_node(x, y, i)
        self.add_node(x2, y2, i2)
        self._graph[frozenset({(x, y), (x2, y2)})] = time

    def remove_node(self, node):
        """
        Remove a node from the graph
        :param node: tuple (x,y) containing the coordinates of the node
        :return:
        """
        self._nodes.pop(node)
        self._graph = {k: v for k, v in self._graph.items() if node not in k}

    def remove_arch_by_coord(self, node_a, node_b):
        """
        Remove an arch from the graph by its nodes coordinates
        :param node_a: tuple (x,y) containing the index and the coordinates of the node a
        :param node_b: tuple (x,y) containing the index and the coordinates of the node b
        :return:
        """
        xa, ya = node_a
        xb, yb = node_b
        self._graph.pop(frozenset({(xa, ya), (xb, yb)}))

    def _remove_arch_by_index(self, ia, ib):
        """
        Remove an arch from the graph by its nodes indexes
        :param ia: index of node a
        :param ib: index of node b
        :return:
        """
        inv_graph = {v: k for k, v in self._graph.items()}
        xa, ya = inv_graph.get(ia)
        xb, yb = inv_graph.get(ib)
        self._graph.pop(frozenset({(ia, xa, ya), (ib, xb, yb)}))

    def held_karp(self, v: (float, float, int), s: frozenset(), zero_node: (float, float, int), d: dict(),
                  pred: dict()):

        # Base case
        if len(s) is 1 and v in self.get_node_list():

            print("Base case:", v, zero_node)
            coordv, _ = v
            coordz, _ = zero_node
            return self._graph[frozenset({coordv, coordz})]
            # S contiene un unico elemento che è v, stiamo andando da 0 --> v

        else:

            try:
                return d[v, s]

            except KeyError:
                min_dist = float(inf)
                min_prec = None
                s1 = frozenset({u for u in s if u != v})

                for u in s1:
                    dist = self.held_karp(u, s1, zero_node, d, pred)  # recursive call
                    print("Dist:", dist)

                    if dist + self._graph[({u, v})] < min_dist:  # update
                        min_dist = dist + self._graph[frozenset({u, v})]
                        min_prec = u

                d[(v, s)] = min_dist
                pred[(v, s)] = min_prec

                return min_dist
