import unittest

import pytest

from LibGraph.PIIndirectGraph import PIIndirectGraph


class TestPIIndirectGraph(unittest.TestCase):

    def test_no_loops(self):
        with pytest.raises(Exception):
            g = PIIndirectGraph()
            g.add_arch(1, 1)

    def test_append_and_get(self):
        g = PIIndirectGraph()
        g.add_arch(1, 2)
        g.add_arch(1, 3)
        g.add_arch(1, 3)
        g.add_arch(3, 1)
        g.add_arch(3, 2)

        g.add_node(4)

        self.assertEqual(g.get_node_list(), {1, 2, 3, 4})
        self.assertEqual(g.get_arch_list(), {(1, 2), (1, 3), (2, 3)})

        g.remove_arch(2, 1)

        self.assertEqual(g.get_node_list(), {1, 2, 3, 4})
        self.assertEqual(g.get_arch_list(), {(1, 3), (2, 3)})

        g.remove_node(3)
        g.remove_node(5)

        self.assertEqual(g.get_node_list(), {1, 2, 4})
        self.assertEqual(g.get_arch_list(), set())

    def test_remove(self):
        g = PIIndirectGraph()
        g.add_arch(1, 2)
        g.add_arch(1, 3)
        g.add_arch(1, 3)
        g.add_arch(3, 1)
        g.add_arch(3, 2)

        self.assertEqual(g.get_adj_list(1), {(1, 2), (1, 3)})

    def test_node_degree(self):
        g = PIIndirectGraph()

        g.add_arch(4, 1)
        g.add_arch(5, 1)
        g.add_arch(6, 1)

        g.add_arch(1, 2)
        g.add_arch(1, 3)
        g.add_arch(1, 4)
        g.add_arch(1, 5)

        self.assertEqual(g.get_node_degree(1), 5)
        self.assertEqual(g.get_node_degree(4), 1)
        self.assertEqual(g.get_node_degree(7), 0)
