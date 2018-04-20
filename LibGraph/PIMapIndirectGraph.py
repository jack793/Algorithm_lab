from LibGraph.PIIndirectGraph import PIIndirectGraph


class PIMapIndirectGraph:
    def __init__(self):
        self._time = dict()
        self._graph = PIIndirectGraph()

    def add_arch(self, node_a, node_b, time):
        self._graph.add_arch(node_a, node_b)
        self._time[frozenset({node_a, node_b})] = time

    def get_arch_list(self):
        arch_list = self._graph.get_arch_list()
        return frozenset({(a, b, self._time[frozenset({a, b})]) for a, b in arch_list})

    def remove_arch(self, node_a, node_b):
        self._graph.remove_arch(node_a, node_b)
        self._time.pop(frozenset({node_a, node_b}))
