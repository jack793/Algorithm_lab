import unittest

from LibGraph.PIMapIndirectGraph import PIMapIndirectGraph


class TestPIMapIndirectGraph(unittest.TestCase):

    def test_add_arch(self):
        graph = PIMapIndirectGraph()

        graph.add_arch((5, 7), (6, 2), 3)
        graph.add_arch((4, 1), (8, 3), 7)
        graph.add_arch((4, 8), (6, 2), 3)

        self.assertEqual(
            {(frozenset({(6, 2), (5, 7)}), 3), (frozenset({(6, 2), (4, 8)}), 3), (frozenset({(8, 3), (4, 1)}), 7)}
            , graph.get_arch_list())

        graph.remove_arch((5, 7), (6, 2))

        self.assertEqual({(frozenset({(6, 2), (4, 8)}), 3), (frozenset({(8, 3), (4, 1)}), 7)}, graph.get_arch_list())
        self.assertEqual({(8, 3), (4, 8), (5, 7), (6, 2), (4, 1)}, graph.get_node_list())

        print("skfm")
        print(graph.get_arch_list())
        print(graph.get_node_list())

        graph.remove_node((6, 2))

        print(graph.get_arch_list())
        print(graph.get_node_list())
