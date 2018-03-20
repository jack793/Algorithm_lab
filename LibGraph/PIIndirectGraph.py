from collections import namedtuple

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

    def undirected_connected_components(self, G):
        CC = set()
        for v in G:
            for i in CC:
                if v not in CC[i]:
                    comp = 



    def get_dfs_path_from_node(self, node):
        if node not in self.get_node_list():
            return namedtuple("DFS", ["path", "predecessors"])(
                set(), dict((k, None) for k in self.get_node_list()))

        def rec(current_node, predecessor_node, nodes_visited, nodes_predecessors):
            if current_node not in nodes_visited:
                nodes_visited.add(current_node)
                nodes_predecessors[current_node] = predecessor_node

                for neighbour in self.get_adj_list(current_node):
                    nodes_visited, nodes_predecessors = rec(neighbour, current_node, nodes_visited, nodes_predecessors)

            return namedtuple("DFS", ["path", "predecessors"])(nodes_visited, nodes_predecessors)

        return rec(node, None, set(), dict())
