from random import random


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
                    g.append(u, v)
        return g


class _PIGraph:
    def __init__(self):
        self._adjList = {}


class PIIndirectGraph(_PIGraph):

    def append(self, node_a, node_b):
        if node_a == node_b:
            raise Exception("Same node arches are not supported")

        if node_a in self._adjList:
            self._adjList[node_a].add(node_b)
        elif node_b in self._adjList:
            self._adjList[node_b].add(node_a)
        else:
            self._adjList[min(node_a, node_b)] = {max(node_a, node_b)}

        # if node_b not in self._adjList:
        #     if node_a in self._adjList:
        #         self._adjList[node_a].add(node_b)
        #     else:
        #         self._adjList[min(node_a, node_b)] = {max(node_a, node_b)}
        #
        # else:
        #     self._adjList[min(node_a, node_b)] = {max(node_a, node_b)}

    def remove(self, from_node, to_node):
        if to_node in self._adjList:
            self._adjList[to_node].remove(from_node)
        if from_node in self._adjList:
            self._adjList[from_node].remove(to_node)

    def adj_list(self):
        """
        Returns a set of tuples containing
        :return:
        """
        return {(min(k, v), max(k, v)) for v in self._adjList
                for k in self._adjList[v]}

    def degree(self, node):
        return len({(k, v) for (k, v) in self.adj_list() if (k == node)}) + len(
            {(k, v) for (k, v) in self.adj_list() if (v == node)})


class PIDirectGraph(_PIGraph):

    def append(self, from_node, to_node):
        if from_node == to_node:
            raise Exception("Same node arches are not supported")
        if to_node not in self._adjList:
            self._adjList[to_node] = {from_node}
        else:
            self._adjList[to_node].add(from_node)

    def remove(self, from_node, to_node):
        if to_node in self._adjList:
            self._adjList[to_node].remove(from_node)

    def adj_list(self):
        """
        Returns a set of tuples containing 
        :return: 
        """
        return {(k, v) for v in self._adjList
                for k in self._adjList[v]}

    def in_degree(self, node) -> int:
        """
        Search for a node in the graph and returns its in degree
        :param node: node to search in the graph
        :return: in degree of the node, if present, zero otherwise
        """
        if node in self._adjList:
            return len(self._adjList[node])
        else:
            return 0

    def out_degree(self, node) -> int:
        """
        Search for a node in the graph and returns its out degree
        :param node: node to search in the graph
        :return: out degree of the node, if present, zero otherwise
        """
        return len({(a, b) for (a, b) in self.adj_list() if a == node})
