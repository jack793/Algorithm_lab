class PIGraph:

    def __init__(self):
        self._adjList = dict()
        self._nodeList = set()

    def add_node(self, node):
        self._nodeList.add(node)

    def remove_node(self, node):
        try:
            self._nodeList.remove(node)
        except KeyError:
            pass
        try:
            self._adjList.pop(node)
        except KeyError:
            pass

        for k in self._adjList:
            try:
                self._adjList[k].remove(node)
            except KeyError:
                pass

    def get_node_list(self) -> set:
        return self._nodeList

    def add_arch(self, node_a, node_b):
        if node_a == node_b:
            raise Exception("Same node arches are not supported")

        self.add_node(node_a)
        self.add_node(node_b)

        if node_b not in self._adjList:
            self._adjList[node_b] = {node_a}
        else:
            self._adjList[node_b].add(node_a)

    def remove_arch(self, node_from, node_to):
        try:
            self._adjList[node_to].remove(node_from)
        except KeyError:
            pass

        try:
            self._adjList[node_to].remove(node_from)
        except KeyError:
            pass

    def get_arch_list(self):
        pass

    def get_adj_list(self, node) -> set:
        pass

    def get_node_degree(self, node):
        return len(self.get_adj_list(node))
