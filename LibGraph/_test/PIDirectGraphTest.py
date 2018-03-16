import unittest

import pytest

from LibGraph.PIDirectGraph import PIDirectGraph


class TestPIDirectGraph(unittest.TestCase):

    def test_no_loops(self):
        with pytest.raises(Exception):
            g = PIDirectGraph()
            g.add_arch(1, 1)

    def test_append_and_get(self):
        g = PIDirectGraph()
        g.add_arch(1, 2)
        g.add_arch(1, 3)
        g.add_arch(1, 3)
        g.add_arch(3, 1)
        g.add_arch(3, 2)

        g.add_node(4)

        self.assertEqual(g.get_node_list(), {1, 2, 3, 4})
        self.assertEqual(g.get_arch_list(), {(1, 2), (1, 3), (3, 1), (3, 2)})

        g.remove_arch(1, 2)

        self.assertEqual(g.get_node_list(), {1, 2, 3, 4})
        self.assertEqual(g.get_arch_list(), {(3, 2), (1, 3), (3, 1)})

        g.remove_node(1)
        g.remove_node(5)

        self.assertEqual(g.get_node_list(), {2, 3, 4})
        self.assertEqual(g.get_arch_list(), {(3, 2)})

    def test_in_out_adj_list(self):
        g = PIDirectGraph()
        g.add_arch(1, 2)
        g.add_arch(1, 3)
        g.add_arch(1, 3)
        g.add_arch(3, 1)
        g.add_arch(3, 2)

        self.assertEqual(g.get_adj_list(1), {(1, 2), (1, 3), (3, 1)})
        self.assertEqual(g.get_in_adj_list(1), {3})
        self.assertEqual(g.get_out_adj_list(1), {2, 3})

    def test_node_degree(self):
        g = PIDirectGraph()

        g.add_arch(4, 1)
        g.add_arch(5, 1)
        g.add_arch(6, 1)

        g.add_arch(1, 2)
        g.add_arch(1, 3)
        g.add_arch(1, 4)
        g.add_arch(1, 5)

        self.assertEqual(g.get_node_degree(1), 7)
        self.assertEqual(g.get_node_degree(8), 0)

        self.assertEqual(g.get_node_in_degree(1), 3)
        self.assertEqual(g.get_node_in_degree(4), 1)

        self.assertEqual(g.get_node_out_degree(1), 4)
        self.assertEqual(g.get_node_out_degree(4), 1)