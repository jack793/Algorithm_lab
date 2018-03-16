from LibGraph.PIGraph import PIGraph


class PIIndirectGraph(PIGraph):

    def get_arch_list(self):
        super().get_arch_list()
        r = set()
        for b in self._adjList:
            for a in self._adjList[b]:
                r.add((min(a, b), max(a, b)))
        return r

    def get_adj_list(self, node):
        super().get_adj_list(node)
        return {(min(a, b), max(a, b)) for (a, b) in self.get_arch_list() if a == node or b == node}

    def get_node_degree(self, node):
        return super().get_node_degree(node)

    def remove_arch(self, node_a, node_b):
        super().remove_arch(node_a, node_b)
        super().remove_arch(node_b, node_a)
