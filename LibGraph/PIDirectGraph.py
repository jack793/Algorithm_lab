import math
from collections import deque, namedtuple

from LibGraph.PIGraph import PIGraph


class PIDirectGraph(PIGraph):

    def add_arch(self, node_from, node_to):
        super().add_arch(node_from, node_to)

    def get_arch_list(self):
        adj_list_items = self.get_raw_adj_list().items()
        return set({(a, b) for (b, r) in adj_list_items for a in r})

    def get_reversed_arch_list(self):
        adj_list_items = self.get_raw_adj_list().items()
        return set({(b, a) for (b, r) in adj_list_items for a in r})

    def get_in_adj_list(self, node):
        # return {a for (a, b) in self.get_arch_list() if node == b}
        try:
            return self._adjList[node]
        except KeyError:
            return set()

    def get_out_adj_list(self, node):
        arch_list = self.get_arch_list()
        return {b for (a, b) in arch_list if node == a}

    def get_adj_list(self, node):
        super().get_adj_list(node)
        arch_list = self.get_arch_list()
        return {(a, b) for (a, b) in arch_list if node == a or node == b}

    def get_node_in_degree(self, node):
        arch_list = self.get_arch_list()
        return len({(a, b) for (a, b) in arch_list if node == b})

    def get_node_out_degree(self, node):
        adj_list = self.get_raw_adj_list()
        try:
            return len(adj_list[node])
        except KeyError:
            return 0

    def get_bfs_path_from_node(self, node):
        nodes_colors = dict()
        nodes_distances = dict()
        nodes_predecessors = dict()

        node_list = self.get_node_list()

        for n in node_list:
            nodes_colors[n] = 0
            nodes_distances[n] = math.inf
            nodes_predecessors[n] = None

        if node not in node_list:
            return namedtuple("BFS", ["predecessors", "distances", "path"])(
                nodes_predecessors, nodes_distances,
                {k for k, v in nodes_colors.items() if
                 v == 2})

        nodes_colors[node] = 1
        nodes_distances[node] = 0

        q = deque([node])

        while len(q) > 0:
            u = q.popleft()
            for v in self.get_out_adj_list(u):
                if nodes_colors[v] == 0:
                    nodes_colors[v] = 1
                    nodes_distances[v] = nodes_distances[u] + 1
                    nodes_predecessors[v] = u
                    q.append(v)

            nodes_colors[u] = 2

        return namedtuple("BFS", ["predecessors", "distances", "path"])(nodes_predecessors, nodes_distances,
                                                                        {k for k, v in nodes_colors.items() if v == 2})

    def get_dfs_path_from_node(self, node):

        node_list = self.get_node_list()

        if node not in node_list:
            return namedtuple("DFS", ["path", "predecessors"])(set(), dict((k, None) for k in node_list))

        def rec(current_node, predecessor_node, nodes_visited, nodes_predecessors):
            if current_node not in nodes_visited:
                nodes_visited.add(current_node)
                nodes_predecessors[current_node] = predecessor_node

                for neighbour in self.get_out_adj_list(current_node):
                    nodes_visited, nodes_predecessors = rec(neighbour, current_node, nodes_visited, nodes_predecessors)

            return namedtuple("DFS", ["path", "predecessors"])(nodes_visited, nodes_predecessors)

        return rec(node, None, set(), dict())
