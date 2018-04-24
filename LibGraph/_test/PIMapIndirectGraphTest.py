import unittest

from LibGraph.PIMapIndirectGraph import PIMapIndirectGraph


class TestPIMapIndirectGraph(unittest.TestCase):

    def test_add_arch(self):
        graph = PIMapIndirectGraph()

        graph.add_arch((1, 5, 7), (2, 6, 2), 3)
        graph.add_arch((3, 4, 1), (4, 8, 3), 7)
        graph.add_arch((5, 4, 8), (2, 6, 2), 3)

        self.assertEqual(
            {(frozenset({(5, 4, 8), (2, 6, 2)}), 3), (frozenset({(4, 8, 3), (3, 4, 1)}), 7),
             (frozenset({(1, 5, 7), (2, 6, 2)}), 3)}
            , graph.get_arch_list())

        graph.remove_arch_by_coord((1, 5, 7), (2, 6, 2))

        self.assertEqual({(frozenset({(3, 4, 1), (4, 8, 3)}), 7), (frozenset({(2, 6, 2), (5, 4, 8)}), 3)},
                         graph.get_arch_list())
        self.assertEqual({((4, 1), 3), ((4, 8), 5), ((5, 7), 1), ((6, 2), 2), ((8, 3), 4)}, graph.get_node_list())

        graph.remove_node((6, 2))

        self.assertEqual({(frozenset({(4, 8, 3), (3, 4, 1)}), 7), (frozenset({(5, 4, 8), (2, 6, 2)}), 3)},
                         graph.get_arch_list())
        self.assertEqual({((4, 8), 5), ((5, 7), 1), ((8, 3), 4), ((4, 1), 3)}
                         , graph.get_node_list())
