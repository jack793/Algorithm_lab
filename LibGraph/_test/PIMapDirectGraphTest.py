import unittest
from math import inf

import pytest

from LibGraph.PIDirectGraph import PIDirectGraph
from LibGraph.PIMapDirectGraph import PIMapDirectGraph


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
        g = PIMapDirectGraph()
        g.add_arch(1, 2, 0, 0)
        g.add_arch(1, 3, 0, 0)
        g.add_arch(3, 1, 0, 0)
        g.add_arch(3, 2, 0, 0)

        self.assertSetEqual(g.get_adj_list(1), {(1, 2), (1, 3), (3, 1)})
        self.assertSetEqual(g.get_in_adj_list(1), {3})
        self.assertSetEqual(g.get_in_adj_list(4), set())
        self.assertSetEqual(g.get_out_adj_list(1), {2, 3})
        self.assertSetEqual(g.get_out_adj_list(4), set())

    def test_node_degree(self):
        g = PIMapDirectGraph()

        g.add_arch(4, 1, 0, 0)
        g.add_arch(5, 1, 0, 0)
        g.add_arch(6, 1, 0, 0)

        g.add_arch(1, 2, 0, 0)
        g.add_arch(1, 3, 0, 0)
        g.add_arch(1, 4, 0, 0)
        g.add_arch(1, 5, 0, 0)

        self.assertEqual(g.get_node_degree(1), 7)
        self.assertEqual(g.get_node_degree(8), 0)

        self.assertEqual(g.get_node_in_degree(1), 3)
        self.assertEqual(g.get_node_in_degree(4), 1)

        self.assertEqual(g.get_node_out_degree(1), 3)
        self.assertEqual(g.get_node_out_degree(4), 1)

    def test_bfs(self):
        g = PIMapDirectGraph()

        g.add_arch(1, 2, 0, 0)
        g.add_arch(2, 3, 0, 0)
        g.add_arch(1, 4, 0, 0)
        g.add_arch(4, 5, 0, 0)
        g.add_arch(5, 6, 0, 0)
        g.add_arch(6, 4, 0, 0)
        g.add_arch(3, 6, 0, 0)

        res = g.get_bfs_path_from_node(1)

        self.assertDictEqual(res.predecessors, {1: None, 2: 1, 3: 2, 4: 1, 5: 4, 6: 3})
        self.assertDictEqual(res.distances, {1: 0, 2: 1, 3: 2, 4: 1, 5: 2, 6: 3})
        self.assertSetEqual(res.path, {1, 2, 3, 4, 5, 6})

        res = g.get_bfs_path_from_node(6)

        self.assertDictEqual(res.predecessors, {1: None, 2: None, 3: None, 4: 6, 5: 4, 6: None})
        self.assertDictEqual(res.distances, {1: inf, 2: inf, 3: inf, 4: 1, 5: 2, 6: 0})
        self.assertSetEqual(g.get_bfs_path_from_node(6).path, {4, 5, 6})

        res = g.get_bfs_path_from_node(7)

        self.assertDictEqual(res.predecessors, {1: None, 2: None, 3: None, 4: None, 5: None, 6: None})
        self.assertDictEqual(res.distances, {1: inf, 2: inf, 3: inf, 4: inf, 5: inf, 6: inf})
        self.assertSetEqual(res.path, set())

    def test_dfs(self):
        g = PIMapDirectGraph()

        g.add_arch(1, 2, 0, 0)
        g.add_arch(2, 3, 0, 0)
        g.add_arch(1, 4, 0, 0)
        g.add_arch(4, 5, 0, 0)
        g.add_arch(5, 6, 0, 0)
        g.add_arch(6, 4, 0, 0)
        g.add_arch(3, 6, 0, 0)

        nodes_visited, nodes_predecessors = g.get_dfs_path_from_node(1)

        self.assertSetEqual(nodes_visited, {1, 2, 3, 4, 5, 6})
        self.assertDictEqual(nodes_predecessors, {1: None, 2: 1, 3: 2, 6: 3, 4: 6, 5: 4})

        nodes_visited, nodes_predecessors = g.get_dfs_path_from_node(6)

        self.assertSetEqual(nodes_visited, {4, 5, 6})
        self.assertDictEqual(nodes_predecessors, {6: None, 4: 6, 5: 4})

        nodes_visited, nodes_predecessors = g.get_dfs_path_from_node(7)

        self.assertSetEqual(nodes_visited, set())
        self.assertDictEqual(nodes_predecessors, {1: None, 2: None, 3: None, 4: None, 5: None, 6: None})

    def test_dijkstra(self):
        g = PIMapDirectGraph()

        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_node(6)
        g.add_node(7)

        g.add_arch(2, 1, 2, 0)
        g.add_arch(2, 6, 2, 0)
        g.add_arch(3, 2, 12, 0)
        g.add_arch(3, 7, 7, 0)
        g.add_arch(4, 3, 3, 0)
        g.add_arch(4, 7, 4, 0)
        g.add_arch(5, 4, 6, 0)
        g.add_arch(5, 7, 8, 0)
        g.add_arch(6, 5, 10, 0)
        g.add_arch(6, 1, 3, 0)
        g.add_arch(7, 2, 5, 0)
        g.add_arch(7, 6, 0, 0)

        distances, predecessors = g.get_sssp_dijkstra(4)

        self.assertEqual(distances[1], 7)
        self.assertEqual(distances[2], 9)
        self.assertEqual(distances[3], 3)
        self.assertEqual(distances[4], 0)
        self.assertEqual(distances[5], 14)
        self.assertEqual(distances[6], 4)
        self.assertEqual(distances[7], 4)

        self.assertEqual(predecessors.get(1), 6)
        self.assertEqual(predecessors.get(2), 7)
        self.assertEqual(predecessors.get(3), 4)
        self.assertEqual(predecessors.get(4), None)
        self.assertEqual(predecessors.get(5), 6)
        self.assertEqual(predecessors.get(6), 7)
        self.assertEqual(predecessors.get(7), 4)

    def test_ccrp(self):
        g = PIMapDirectGraph()

        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_node(6)
        g.add_node(7)

        g.add_arch(2, 1, 2, 100)
        g.add_arch(2, 6, 2, 100)
        g.add_arch(3, 2, 12, 100)
        g.add_arch(3, 7, 7, 100)
        g.add_arch(4, 3, 3, 100)
        g.add_arch(4, 7, 4, 100)
        g.add_arch(5, 4, 6, 100)
        g.add_arch(5, 7, 8, 100)
        g.add_arch(6, 5, 10, 100)
        g.add_arch(6, 1, 3, 100)
        g.add_arch(7, 2, 5, 100)
        g.add_arch(7, 6, 0, 100)

        res = g.ccrp({4}, {1}, 100)
