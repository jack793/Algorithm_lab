import unittest

from LibGraph.PIGraph import *


class TestER(unittest.TestCase):
    def test_something(self):
        return True  # TODO er direct e undirect


class TestDPA(unittest.TestCase):
    def test_dpa_generation(self):
        g = PIGraph.gen_direct_graph_dpa(2, 4)
        print(g.adj_list())

class TestUPA(unittest.TestCase):
    def test_upa_generation(self):
        g = PIGraph.gen_direct_graph_upa(2, 4)
        print(g.adj_list())

if __name__ == '__main__':
    unittest.main()
