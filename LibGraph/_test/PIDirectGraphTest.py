import unittest
from math import inf

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

        self.assertSetEqual(g.get_node_list(), {1, 2, 3, 4})
        self.assertSetEqual(g.get_arch_list(), {(1, 2), (1, 3), (3, 1), (3, 2)})
        self.assertSetEqual(g.get_reversed_arch_list(), {(1, 3), (3, 1), (2, 3), (2, 1)})

        g.remove_arch(1, 2)

        self.assertSetEqual(g.get_node_list(), {1, 2, 3, 4})
        self.assertSetEqual(g.get_arch_list(), {(3, 2), (1, 3), (3, 1)})
        self.assertSetEqual(g.get_reversed_arch_list(), {(1, 3), (3, 1), (2, 3)})

        g.remove_node(1)
        g.remove_node(5)

        self.assertSetEqual(g.get_node_list(), {2, 3, 4})
        self.assertSetEqual(g.get_arch_list(), {(3, 2)})
        self.assertSetEqual(g.get_reversed_arch_list(), {(2, 3)})

    def test_in_out_adj_list(self):
        g = PIDirectGraph()
        g.add_arch(1, 2)
        g.add_arch(1, 3)
        g.add_arch(1, 3)
        g.add_arch(3, 1)
        g.add_arch(3, 2)

        self.assertSetEqual(g.get_adj_list(1), {(1, 2), (1, 3), (3, 1)})
        self.assertSetEqual(g.get_in_adj_list(1), {3})
        self.assertSetEqual(g.get_in_adj_list(4), set())
        self.assertSetEqual(g.get_out_adj_list(1), {2, 3})
        self.assertSetEqual(g.get_out_adj_list(4), set())

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

    def test_bfs(self):
        g = PIDirectGraph()

        g.add_arch(1, 2)
        g.add_arch(2, 3)
        g.add_arch(1, 4)
        g.add_arch(4, 5)
        g.add_arch(5, 6)
        g.add_arch(6, 4)
        g.add_arch(3, 6)

        self.assertDictEqual(g.get_bfs_path_from_node(1)['predecessors'], {1: None, 2: 1, 3: 2, 4: 1, 5: 4, 6: 3})
        self.assertDictEqual(g.get_bfs_path_from_node(1)['distances'], {1: 0, 2: 1, 3: 2, 4: 1, 5: 2, 6: 3})
        self.assertSetEqual(g.get_bfs_path_from_node(1)['path'], {1, 2, 3, 4, 5, 6})

        self.assertDictEqual(g.get_bfs_path_from_node(6)['predecessors'],
                             {1: None, 2: None, 3: None, 4: 6, 5: 4, 6: None})
        self.assertDictEqual(g.get_bfs_path_from_node(6)['distances'],
                             {1: inf, 2: inf, 3: inf, 4: 1, 5: 2, 6: 0})
        self.assertSetEqual(g.get_bfs_path_from_node(6)['path'], {4, 5, 6})

        self.assertDictEqual(g.get_bfs_path_from_node(7)['predecessors'],
                             {1: None, 2: None, 3: None, 4: None, 5: None, 6: None})
        self.assertDictEqual(g.get_bfs_path_from_node(7)['distances'], {1: inf, 2: inf, 3: inf, 4: inf, 5: inf, 6: inf})
        self.assertSetEqual(g.get_bfs_path_from_node(7)['path'], set())
