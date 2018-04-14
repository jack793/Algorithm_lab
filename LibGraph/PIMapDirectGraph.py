from collections import defaultdict
from copy import copy
from heapq import heappush, heappop
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
        try:
            self._time[node_from].pop(node_to)
        except KeyError:
            pass
        try:
            self._capacity[node_from].pop(node_to)
        except KeyError:
            pass
        try:
            self._graph.remove_arch(node_from, node_to)
        except KeyError:
            pass

    def add_node(self, node):
        self._graph.add_node(node)

    def remove_node(self, node):
        try:
            self._capacity.pop(node)
        except KeyError:
            pass
        try:
            self._time.pop(node)
        except KeyError:
            pass
        for node_from in self._capacity:
            try:
                self._capacity[node_from].pop(node)
            except KeyError:
                pass
        for node_from in self._time:
            try:
                self._time[node_from].pop(node)
            except KeyError:
                pass
        self._graph.remove_node(node)

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

    def get_sssp_dijkstra(self, source_node, ) -> (set(), dict()):
        """
        Find the shortest predecessors from a source node to any other accessible node
        :param source_node: Node from which start the search
        :return tuple containing the set of distances of the nodes from the source and a
        dictionary of the predecessors of each node visited
        """

        distances = defaultdict()
        predecessors = defaultdict()
        heap = [(0, source_node, None)]
        while heap:

            print(len(heap))  # TODO: remove, just for "production"

            path_len, v, pred_node = heappop(heap)
            if distances.get(v) is None:
                distances[v] = path_len
                predecessors[v] = pred_node
                for w in self._graph.get_out_adj_list(v):
                    edge_len = self._time[v][w]
                    if distances.get(w) is None:
                        heappush(heap, (path_len + edge_len, w, v))

        return distances, predecessors

    def ccrp(self, source_nodes: set(), destination_nodes: set()):
        """
        Capacity Constrained Route Planner: this method finds the the best paths from a set of sources to a set of
        destinations, choosing always the shortest path (time) and taking account of the capacity of each one.
        :param source_nodes:  set of source nodes
        :param destination_nodes: set of destination nodes
        :return: set of paths
        """
        # graph = copy(self)
        #
        # # Find a valid super source
        # v0 = int(max(graph.get_node_list())) + 1
        #
        # # Add super source to the graph
        # self.add_node(v0)
        #
        # # Connect super source to the original sources
        # for node in source_nodes:
        #     graph.add_arch(v0, node, 0, inf)
        #
        # plan = []
        # capacities = []
        # times = []
        #
        # while True:
        #     distances, predecessors = self.get_sssp_dijkstra(v0)
        #
        #     try:
        #         min_time_destination = min(destination_nodes, key=lambda v: distances[v])
        #     except KeyError:
        #         break
        #
        #     times.append(distances[min_time_destination])
        #
        #     path = [min_time_destination]
        #     while True:
        #         last = path[-1]
        #         p = predecessors.get(last)
        #         if p is not None:
        #             path.append(p)
        #         elif last is not v0:
        #             path.clear()
        #             break
        #         else:
        #             break
        #
        #     min_cap = inf
        #     for i in path:
        #         try:
        #             if min_cap > graph._capacity[predecessors.get(i)][i]:
        #                 min_cap = graph._capacity[predecessors.get(i)][i]
        #         except KeyError:
        #             pass
        #
        #     capacities.append(min_cap)
        #
        #     for i in path:
        #         try:
        #             graph._capacity[predecessors.get(i)][i] = graph._capacity[predecessors.get(i)][i] - min_cap
        #             if graph._capacity[predecessors.get(i)][i] is 0:
        #                 graph.remove_arch(predecessors.get(i), i)
        #         except KeyError:
        #             pass
        #
        #     path.remove(v0)
        #     path = list(reversed(path))
        #     plan.append(path)
        # return plan, capacities, times

        # Copy of the original graph
        g = copy(self)

        # Add super source node
        super_source_node = max(g._graph.get_node_list()) + 1
        g.add_node(super_source_node)
        for source in source_nodes:
            g.add_arch(super_source_node, source, 0, inf)

        # Create plan set
        plan = list()
        capacities = list()
        times = list()

        while True:

            distances, predecessors = g.get_sssp_dijkstra(super_source_node)
            distances_destinations = filter(lambda k: k in destination_nodes, distances)

            try:
                min_distance_node = min(distances_destinations, key=lambda k: distances.get(k))
            except ValueError:
                break

            # Add distance to the result
            times.append(distances.get(min_distance_node))

            path = list()

            # Populate the path
            last_node = min_distance_node
            while True:
                # Add the last node
                path.append(last_node)

                # If there are any predecessor nodes left, continue
                if predecessors.get(last_node) is not None:
                    last_node = predecessors.get(last_node)
                else:
                    break
            path = list(reversed(path[:-1]))

            # Find least capacity in the path (bottleneck)
            bottleneck = inf
            for i in range(len(path)):
                try:
                    if bottleneck > g._capacity[path[i]][path[i + 1]]:
                        bottleneck = g._capacity[path[i]][path[i + 1]]
                except KeyError:
                    pass

                # TODO: possible solution
                except IndexError:
                    pass

            # Add bottleneck to the capacities result
            capacities.append(bottleneck)

            # Update capacity of the arches
            for i in range(len(path)):
                try:
                    # Update arch capacity
                    g._capacity[path[i]][path[i + 1]] -= bottleneck

                    # Remove the arch if full capacity
                    if g._capacity[path[i]][path[i + 1]] is 0:
                        g.remove_arch(path[i], path[i + 1])
                except KeyError:
                    pass

                # TODO: possible solution
                except IndexError:
                    pass

            # Remove node if all arches are gone
            if len(g.get_in_adj_list(min_distance_node)) is 0:
                g.remove_node(min_distance_node)

            # Add path to the plan result
            plan.append(path)

        return plan, capacities, times
