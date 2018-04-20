import unittest

from LibGraph.PIMapIndirectGraph import PIMapIndirectGraph


class TestPIMapIndirectGraph(unittest.TestCase):

    def test_add_arch(self):
        graph = PIMapIndirectGraph()

        graph.add_arch((5, 7), (6, 2), 3)
        graph.add_arch((4, 1), (8, 3), 7)
        graph.add_arch((4, 8), (6, 2), 3)

        print(graph.get_arch_list())

        self.assertEqual(frozenset({((4, 1), (8, 3), 7), ((5, 7), (6, 2), 3), ((4, 8), (6, 2), 3)}), graph.get_arch_list())

        graph.remove_arch((5, 7), (6, 2))

        print(graph.get_arch_list())