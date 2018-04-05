import heapq
from collections import defaultdict
from math import inf

from LibGraph.PIDirectGraph import PIDirectGraph


class PIMapDirectGraph:

    def __init__(self):
        self._graph = PIDirectGraph()
        self._time = dict()
        self._capacity = dict()

    def get_node_list(self):
        return self._graph.get_node_list()

    def get_arch_list(self):
        arch_list = self._graph.get_arch_list()
        return set((a, b, self._time[a][b], self._capacity[a][b]) for a, b in arch_list)

    def add_arch(self, node_from, node_to, time, capacity):
        self._graph.add_arch(node_from, node_to)
        if node_from not in self._time:
            self._time[node_from] = dict()
            self._time[node_from][node_to] = time
        elif node_to not in self._time[node_from]:
            self._time[node_from][node_to] = time
        else:
            raise KeyError("Time already set for the arch")

        if node_from not in self._capacity:
            self._capacity[node_from] = dict()
            self._capacity[node_from][node_to] = capacity
        elif node_to not in self._capacity[node_from]:
            self._capacity[node_from][node_to] = capacity
        else:
            raise KeyError("Capacity already set for the arch")

    def remove_arch(self, node_from, node_to):
        self._time[node_from].remove(node_to)
        self._capacity[node_from].remove(node_to)
        self._graph.remove_arch(node_from, node_to)

    def add_node(self, node):
        self._graph.add_node(node)

    def remove_node(self, node):
        self._capacity.pop(node)
        self._time.pop(node)
        for node_from in self._capacity:
            self._capacity[node_from].pop(node)
        for node_from in self._time:
            self._time[node_from].pop(node)
        self._graph.remove_node(node)

    def get_sssp_dijkstra(self, source_node: object) -> (set(), dict()):
        """
        Find the shortest predecessors from a source node to any other accessible node :param source_node: Node from
        which start the search :return tuple containing the set of distances of the nodes from the source and a
        dictionary of the predecessors of each node visited
        """

        distances = {source_node: 0}
        heap = [(0, source_node)]
        predecessors = defaultdict()

        nodes = set(self.get_node_list())

        while nodes and heap:
            current_weight, min_node = heapq.heappop(heap)

            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(heap)

            nodes.remove(min_node)

            for v in self._graph.get_out_adj_list(min_node):
                weight = current_weight + self._time[min_node][v]
                if v not in distances or weight < distances[v]:
                    distances[v] = weight
                    heapq.heappush(heap, (weight, v))
                    predecessors[v] = min_node

        return distances, predecessors

    def ccrp(self, source_nodes: set(), destination_nodes: set()):
        super_node_index = max(self.get_node_list()) + 1

        self.add_node(super_node_index)  # add super_source to node_list

        for i in source_nodes:
            self.add_arch(super_node_index, source_nodes[i], 0, inf)

        plan = set()
        distances, predecessors = self.get_sssp_dijkstra(super_node_index)

        for d in destination_nodes:
            path = []
            try:
                prec = d
                while prec is not None:
                    path.append(prec)
                    prec = predecessors[prec]
                    if prec in source_nodes:
                        plan.add(reversed(path))
                        break
            except KeyError:
                continue

    def get_node_out_degree(self, node):
        return self._graph.get_node_out_degree(node)

    def get_node_in_degree(self, node):
        return self._graph.get_node_out_degree(node)

    def get_node_degree(self, node):
        return self._graph.get_node_degree(node)

    def get_adj_list(self, node):
        return self._graph.get_adj_list(node)

    def get_in_adj_list(self, node):
        return self._graph.get_in_adj_list(node)

    def get_out_adj_list(self, node):
        return self._graph.get_out_adj_list(node)

    def get_bfs_path_from_node(self, node):
        return self._graph.get_bfs_path_from_node(node)

    def get_dfs_path_from_node(self, node):
        return self._graph.get_dfs_path_from_node(node)
