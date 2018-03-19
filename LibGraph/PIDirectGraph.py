import math
from collections import deque

from LibGraph.PIGraph import PIGraph


class PIDirectGraph(PIGraph):

    def add_arch(self, node_from, node_to):
        super().add_arch(node_from, node_to)

    def get_arch_list(self):
        return set({(a, b) for (b, r) in self._adjList.items() for a in r})

    def get_reversed_arch_list(self):
        return set({(b, a) for (b, r) in self._adjList.items() for a in r})

    def get_in_adj_list(self, node):
        # return {a for (a, b) in self.get_arch_list() if node == b}
        try:
            return self._adjList[node]
        except KeyError:
            return set()

    def get_out_adj_list(self, node):
        return {b for (a, b) in self.get_arch_list() if node == a}

    def get_adj_list(self, node):
        super().get_adj_list(node)
        return {(a, b) for (a, b) in self.get_arch_list() if node == a or node == b}

    def get_node_in_degree(self, node):
        return len({(a, b) for (a, b) in self.get_arch_list() if node == b})

    def get_node_out_degree(self, node):
        return len({(a, b) for (a, b) in self.get_arch_list() if node == a})

    def get_bfs_path_from_node(self, node):
        nodes_colors = dict()
        nodes_distances = dict()
        nodes_predecessors = dict()

        for n in self.get_node_list():
            nodes_colors[n] = 0
            nodes_distances[n] = math.inf
            nodes_predecessors[n] = None

        if node not in self.get_node_list():
            return {
                "predecessors": nodes_predecessors,
                "distances": nodes_distances,
                "path": {k for k, v in nodes_colors.items() if v == 2}
            }

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

        return {
            "predecessors": nodes_predecessors,
            "distances": nodes_distances,
            "path": {k for k, v in nodes_colors.items() if v == 2}
        }

    def get_dfs_path_from_node(self, node):

        if node not in self.get_node_list():
            return set(), dict((k, None) for k in self.get_node_list())

        def rec(current_node, predecessor_node, nodes_visited, nodes_predecessors):
            if current_node not in nodes_visited:
                nodes_visited.add(current_node)
                nodes_predecessors[current_node] = predecessor_node

                for neighbour in self.get_out_adj_list(current_node):
                    nodes_visited, nodes_predecessors = rec(neighbour, current_node, nodes_visited, nodes_predecessors)

            return nodes_visited, nodes_predecessors

        return rec(node, None, set(), dict())
