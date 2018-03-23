from collections import namedtuple, deque
from math import inf

from LibGraph.PIGraph import PIGraph


class PIIndirectGraph(PIGraph):

    def add_arch(self, node_a, node_b):
        super().add_arch(node_a, node_b)
        super().add_arch(node_b, node_a)

    def get_arch_list(self):
        super().get_arch_list()
        r = set()
        for b in self._adjList:
            for a in self._adjList[b]:
                r.add((min(a, b), max(a, b)))
        return r

    def get_adj_list(self, node):
        super().get_adj_list(node)
        try:
            return self.get_raw_adj_list()[node]
        except KeyError:
            return {}

    def get_node_degree(self, node):
        return super().get_node_degree(node)

    def remove_arch(self, node_a, node_b):
        super().remove_arch(node_a, node_b)
        super().remove_arch(node_b, node_a)

    def get_bfs_path_from_node(self, node):
        nodes_colors = dict()
        nodes_distances = dict()
        nodes_predecessors = dict()

        node_list = self.get_node_list()

        for n in node_list:
            nodes_colors[n] = 0
            nodes_distances[n] = inf
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
            adj_u = self.get_adj_list(u)
            for v in adj_u:
                if nodes_colors[v] == 0:
                    nodes_colors[v] = 1
                    nodes_distances[v] = nodes_distances[u] + 1
                    nodes_predecessors[v] = u
                    q.append(v)

            nodes_colors[u] = 2

        return namedtuple("BFS", ["predecessors", "distances", "path"])(
            nodes_predecessors, nodes_distances,
            {k for k, v in nodes_colors.items() if v == 2})

    def get_dfs_path_from_node(self, node):
        node_list = self.get_node_list()
        if node not in node_list:
            return namedtuple("DFS", ["path", "predecessors"])(
                set(), dict((k, None) for k in node_list))

        def rec(current_node, predecessor_node, nodes_visited, nodes_predecessors):
            if current_node not in nodes_visited:
                nodes_visited.add(current_node)
                nodes_predecessors[current_node] = predecessor_node

                node_adj = self.get_adj_list(current_node)
                for neighbour in node_adj:
                    nodes_visited, nodes_predecessors = rec(neighbour, current_node, nodes_visited, nodes_predecessors)

            return namedtuple("DFS", ["path", "predecessors"])(nodes_visited, nodes_predecessors)

        return rec(node, None, set(), dict())

    def get_connected_components(self):
        connected_components = set()
        node_list = self.get_node_list()
        for v in node_list:
            if v not in {item for component in connected_components for item in component}:
                comp, _ = self.get_dfs_path_from_node(v)
                connected_components.add(frozenset(comp))

        return connected_components

    def get_resilience(self):
        try:
            v = max(self.get_connected_components(), key=len)
            return len(v)
        except ValueError:
            return 0
