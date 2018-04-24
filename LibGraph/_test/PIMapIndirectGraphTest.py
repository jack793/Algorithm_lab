import unittest

import pytest

from LibGraph.PIMapIndirectGraph import PIMapIndirectGraph


class TestPIMapIndirectGraph(unittest.TestCase):
    def test_unfair_node(self):
        with pytest.raises(Exception):
            graph = PIMapIndirectGraph()
            graph.add_node(0, 0, 1)
            graph.add_node(0, 0, 2)

    def test_add_arch(self):
        graph = PIMapIndirectGraph()
        graph.add_node(0, 0, 1)
        graph.add_node(1, 0, 2)
        graph.add_node(0, 1, 3)
        graph.add_node(1, 1, 4)

        self.assertEqual({((1, 1), 4), ((0, 1), 3), ((0, 0), 1), ((1, 0), 2)}, graph.get_node_list())
        self.assertEqual(set(), graph.get_arch_list())

        graph.add_arch((0, 0, 1), (1, 1, 4), 5)
        graph.add_arch((0, 1, 3), (1, 0, 2), 3)

        self.assertEqual({((1, 1), 4), ((0, 1), 3), ((0, 0), 1), ((1, 0), 2)}, graph.get_node_list())
        self.assertEqual({(frozenset({(1, 0), (0, 1)}), 3), (frozenset({(0, 0), (1, 1)}), 5)},
                         graph.get_arch_list())

        graph.add_arch((2, 0, 5), (2, 2, 6), 7)
        graph.add_arch((0, 2, 7), (2, 0, 5), 9)

        self.assertEqual({((2, 0), 5), ((0, 2), 7), ((0, 1), 3), ((0, 0), 1), ((1, 0), 2), ((1, 1), 4), ((2, 2), 6)},
                         graph.get_node_list())
        self.assertEqual({(frozenset({(2, 0), (0, 2)}), 9), (frozenset({(1, 0), (0, 1)}), 3),
                          (frozenset({(2, 0), (2, 2)}), 7), (frozenset({(0, 0), (1, 1)}), 5)},
                         graph.get_arch_list())

        graph.remove_arch_by_coord((2, 0), (2, 2))

        self.assertEqual({((2, 0), 5), ((0, 2), 7), ((0, 1), 3), ((0, 0), 1), ((1, 0), 2), ((1, 1), 4), ((2, 2), 6)},
                         graph.get_node_list())
        self.assertEqual(
            {(frozenset({(0, 0), (1, 1)}), 5), (frozenset({(2, 0), (0, 2)}), 9), (frozenset({(0, 1), (1, 0)}), 3)},
            graph.get_arch_list())

        graph.remove_node((2, 0))

        self.assertEqual({((0, 2), 7), ((0, 1), 3), ((0, 0), 1), ((1, 0), 2), ((1, 1), 4), ((2, 2), 6)},
                         graph.get_node_list())
        self.assertEqual({(frozenset({(0, 0), (1, 1)}), 5), (frozenset({(0, 1), (1, 0)}), 3)},
                         graph.get_arch_list())
