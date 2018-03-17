from LibGraph.PIGraph import PIGraph


class PIDirectGraph(PIGraph):

    def add_arch(self, node_from, node_to):
        super().add_arch(node_from, node_to)

    def get_arch_list(self):
        super().get_arch_list()
        r = set()
        for b in self._adjList:
            for a in self._adjList[b]:
                r.add((a, b))
        return r

    def get_reversed_arch_list(self):
        r = set()
        for b in self._adjList:
            for a in self._adjList[b]:
                r.add((b, a))
        return r

    def get_in_adj_list(self, node):
        return {a for (a, b) in self.get_arch_list() if node == b}

    def get_out_adj_list(self, node):
        return {b for (a, b) in self.get_arch_list() if node == a}

    def get_adj_list(self, node):
        super().get_adj_list(node)
        return {(a, b) for (a, b) in self.get_arch_list() if node == a or node == b}

    def get_node_in_degree(self, node):
        return len({(a, b) for (a, b) in self.get_arch_list() if node == b})

    def get_node_out_degree(self, node):
        return len({(a, b) for (a, b) in self.get_arch_list() if node == a})
