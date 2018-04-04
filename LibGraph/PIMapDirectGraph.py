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
        Find the shortest path from a source node to any other accessible node :param source_node: source of the path
        :param source_node Node from which start from
        :return tuple containing the set of visited nodes and a dictionary of the distance between the source and any
        of the previous nodes
        """

        visited = {source_node: 0}
        heap = [(0, source_node)]
        path = {}

        nodes = set(self.get_node_list())

        i = 0

        while nodes and heap:
            current_weight, min_node = heapq.heappop(heap)

            i += 1
            print(i)

            try:
                while min_node not in nodes:
                    current_weight, min_node = heapq.heappop(heap)
            except IndexError:
                break

            nodes.remove(min_node)

            for v in self._graph.get_out_adj_list(min_node):
                weight = current_weight + self._time[min_node][v]
                if v not in visited or weight < visited[v]:
                    visited[v] = weight
                    heapq.heappush(heap, (weight, v))
                    path[v] = min_node

        return visited, path

    def ccrp(self, source_nodes, destination_nodes):
        i = 0
        while i in self.get_node_list():
            i += 1

        self.add_node(i)  # add super_source to node_list

        for j in source_nodes:
            self.add_arch(i, source_nodes[j], 0, inf)

        plan = dict()
        _, predecessors = self.get_sssp_dijkstra(i)

        ##### DA QUI INIZIA IL CICLO REPEAT UNTIL PATH != NULL ###
        cont = -1

        for k in destination_nodes:
            path = set()
            z = k
            cont += 1
            while z != i:
                path.add(z)
                z = predecessors[z]

            path.add(z)
            plan[cont] = path  # set of set

        flow = inf

        # se k è vuoto, alla fine plan[cont] = plan[-1] mi deve sollevare un'eccezione che il grafo è vuoto

        for a in range(len(plan[cont]), 1):
            if self._capacity[a][a - 1] < flow:
                flow = self._capacity[a][a - 1]

        for b in range(len(plan[cont]), 1):
            self._capacity[a][a - 1] -= flow
            if self._capacity[a][a - 1] == 0:
                self.remove_arch(a, a - 1)
