import heapq
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

    def get_sssp_dijkstra(self, source_node, target_node):
        time_from_source = dict()
        predecessors = dict()
        initial_node_list = self._graph.get_node_list()

        # INIT_SSSP
        for node in initial_node_list:
            time_from_source[node] = inf
            predecessors[node] = None

        time_from_source[source_node] = 0

        q = []
        for k, v in time_from_source.items():
            heapq.heappush(q, [v, k])

        j = 0
        while len(q) > 0:
            [_, u] = heapq.heappop(q)
            j += 1
            print("i:", j)
            print("n:", u)
            out_adj = self._graph.get_out_adj_list(u)
            for v in out_adj:
                if time_from_source[u] + self._time[u][v] < time_from_source[v]:
                    time_from_source[v] = time_from_source[u] + self._time[u][v]
                    predecessors[v] = u
                    for i in range(len(q)):
                        [k, w] = q[i]
                        if w == v:
                            q[i] = [time_from_source[v], v]
                            heapq._siftup(q, i)
                            break

        return time_from_source, predecessors
