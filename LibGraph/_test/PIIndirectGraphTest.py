import unittest
from math import inf

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

        self.assertSetEqual(g.get_node_list(), {1, 2, 3, 4})
        self.assertSetEqual(g.get_arch_list(), {(1, 2), (1, 3), (2, 3)})

        g.remove_arch(2, 1)

        self.assertSetEqual(g.get_node_list(), {1, 2, 3, 4})
        self.assertSetEqual(g.get_arch_list(), {(1, 3), (2, 3)})

        g.remove_node(3)
        g.remove_node(5)

        self.assertSetEqual(g.get_node_list(), {1, 2, 4})
        self.assertSetEqual(g.get_arch_list(), set())

    def test_remove(self):
        g = PIIndirectGraph()
        g.add_arch(1, 2)
        g.add_arch(1, 3)
        g.add_arch(1, 3)
        g.add_arch(3, 1)
        g.add_arch(3, 2)

        self.assertSetEqual(g.get_adj_list(1), {2, 3})

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

    def test_bfs(self):
        g = PIIndirectGraph()

        g.add_arch(1, 2)
        g.add_arch(2, 3)
        g.add_arch(1, 4)
        g.add_arch(4, 5)
        g.add_arch(5, 6)
        g.add_arch(6, 4)
        g.add_arch(3, 6)

        predecessors, distances, path = g.get_bfs_path_from_node(1)

        self.assertDictEqual(predecessors, {1: None, 2: 1, 3: 2, 4: 1, 5: 4, 6: 4})
        self.assertDictEqual(distances, {1: 0, 2: 1, 3: 2, 4: 1, 5: 2, 6: 2})
        self.assertSetEqual(path, {1, 2, 3, 4, 5, 6})

        predecessors, distances, path = g.get_bfs_path_from_node(6)

        self.assertDictEqual(predecessors, {1: 4, 2: 3, 3: 6, 4: 6, 5: 6, 6: None})
        self.assertDictEqual(distances, {1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 0})
        self.assertSetEqual(path, {1, 2, 3, 4, 5, 6})

        predecessors, distances, path = g.get_bfs_path_from_node(7)

        self.assertDictEqual(predecessors, {1: None, 2: None, 3: None, 4: None, 5: None, 6: None})
        self.assertDictEqual(distances, {1: inf, 2: inf, 3: inf, 4: inf, 5: inf, 6: inf})
        self.assertSetEqual(path, set())

    def test_dfs(self):
        g = PIIndirectGraph()

        g.add_arch(1, 2)
        g.add_arch(2, 3)
        g.add_arch(1, 4)
        g.add_arch(4, 5)
        g.add_arch(5, 6)
        g.add_arch(6, 4)
        g.add_arch(3, 6)

        nodes_visited, nodes_predecessors = g.get_dfs_path_from_node(1)

        self.assertSetEqual(nodes_visited, {1, 2, 3, 4, 5, 6})
        self.assertDictEqual(nodes_predecessors, {1: None, 2: 1, 3: 2, 6: 3, 4: 6, 5: 4})

        nodes_visited, nodes_predecessors = g.get_dfs_path_from_node(6)

        self.assertSetEqual(nodes_visited, {1, 2, 3, 4, 5, 6})
        self.assertDictEqual(nodes_predecessors, {1: 2, 2: 3, 3: 6, 4: 1, 5: 4, 6: None})

        nodes_visited, nodes_predecessors = g.get_dfs_path_from_node(7)

        self.assertSetEqual(nodes_visited, set())
        self.assertDictEqual(nodes_predecessors, {1: None, 2: None, 3: None, 4: None, 5: None, 6: None})

    def test_connected_components(self):
        g = PIIndirectGraph()

        g.add_arch(4, 1)
        g.add_arch(5, 1)
        g.add_arch(6, 1)

        g.add_arch(1, 2)
        g.add_arch(1, 3)
        g.add_arch(1, 4)
        g.add_arch(1, 5)

        self.assertEqual(g.get_connected_components(), {frozenset({1, 2, 3, 4, 5, 6})})
