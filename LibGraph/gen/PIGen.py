from random import random, choice

from LibGraph.PIDirectGraph import PIDirectGraph
from LibGraph.PIIndirectGraph import PIIndirectGraph


class PIGen:
    @staticmethod
    def gen_direct_graph_er(nodes, threshold):
        g = PIDirectGraph()
        for u in range(0, nodes):
            for v in range(0, nodes):
                if u != v:
                    a = random()
                    if a < threshold:
                        g.add_arch(u, v)
        return g

    @staticmethod
    def gen_indirect_graph_er(nodes, threshold):
        g = PIIndirectGraph()
        for u in range(0, nodes):
            for v in range(0, nodes):
                if u != v:
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
                    g.add_arch(a, b)

        trial = DPATrial(m)
        for u in range(m, n):
            new_graph_nodes = trial.run_trial(m)
            graph_nodes.add(u)
            for v in new_graph_nodes:
                g.add_arch(u, v)
        return g

    @staticmethod
    def gen_indirect_graph_upa(m, n):
        class UPATrial:
            _numNodes = 0
            _nodeNumbers = []

            def __init__(self, num_nodes):
                self._numNodes = num_nodes
                self._nodeNumbers = [node for node in range(num_nodes)
                                     for _ in range(num_nodes)]

            def run_trial(self, num_nodes):
                cont = 0
                new_neighbours = set()
                for _ in range(num_nodes):
                    v = choice(self._nodeNumbers)
                    if v not in new_neighbours:
                        cont += 1
                        new_neighbours.add(v)

                for _ in range(0, cont):
                    self._nodeNumbers.append(self._numNodes)

                self._nodeNumbers.extend(list(new_neighbours))
                self._numNodes += 1

                return new_neighbours

        graph_nodes = set(range(0, m))
        g = PIIndirectGraph()
        for a in graph_nodes:
            for b in graph_nodes:
                if a != b:
                    g.add_arch(a, b)
        trial = UPATrial(m)
        for u in range(m, n):
            new_graph_nodes = trial.run_trial(m)
            graph_nodes.add(u)
            for v in new_graph_nodes:
                g.add_arch(u, v)
        return g
