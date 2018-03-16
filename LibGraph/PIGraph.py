from random import random, choice


class PIGraph:
    @staticmethod
    def gen_direct_graph_er(nodes, threshold):
        g = PIDirectGraph()
        for u in range(0, nodes):
            for v in range(0, nodes):
                a = random()
                if a < threshold:
                    g.append(u, v)
        return g

    @staticmethod
    def gen_indirect_graph_er(nodes, threshold):
        g = PIIndirectGraph()
        for u in range(0, nodes):
            for v in range(0, nodes):
                a = random()
                if a < threshold:
                    g.add_arch(u, v)
        return g

    @staticmethod
    def gen_direct_graph_dpa(m, n):

        class DPATrial:
            _numNodes = 0
            _nodeNumbers = []

            def __init__(self, num_nodes):
                self._numNodes = num_nodes
                self._nodeNumbers = [node for node in range(num_nodes)
                                     for _ in range(num_nodes)]

            def run_trial(self, num_nodes):
                new_neighbours = set()
                for _ in range(num_nodes):
                    v = choice(self._nodeNumbers)
                    new_neighbours.add(v)

                self._nodeNumbers.append(self._numNodes)
                self._nodeNumbers.extend(list(new_neighbours))
                self._numNodes += 1

                return new_neighbours

        graph_nodes = set(range(0, m))
        g = PIDirectGraph()
        for a in graph_nodes:
            for b in graph_nodes:
                if a != b:
                    g.append(a, b)

        trial = DPATrial(m)
        for u in range(m, n):
            new_graph_nodes = trial.run_trial(m)
            graph_nodes.add(u)
            for v in new_graph_nodes:
                g.append(u, v)
        return g

    # @staticmethod
    # def gen_indirect_graph_upa(m, n):


class _PIGraph:
    def __init__(self):
        self._adjList = {}
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

    def get_node_list(self):
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

    def get_adj_list(self, node):
        pass


class PIIndirectGraph(_PIGraph):

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
        return len(self.get_adj_list(node))

    def remove_arch(self, node_a, node_b):
        super().remove_arch(node_a, node_b)
        super().remove_arch(node_b, node_a)


class PIDirectGraph(_PIGraph):

    def add_arch(self, node_from, node_to):
        super().add_arch(node_from, node_to)

    def get_arch_list(self):
        r = set()
        for b in self._adjList:
            for a in self._adjList[b]:
                r.add((a, b))
        return r

    def get_in_adj_list(self, node):
        return {(a, b) for (a, b) in self.get_arch_list() if node == b}

    def get_out_adj_list(self, node):
        return {(a, b) for (a, b) in self.get_arch_list() if node == a}
