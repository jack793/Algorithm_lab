import unittest

from LibGraph.gen.PIGen import PIGen


class TestPIGen(unittest.TestCase):
    def test_d_er_generation(self):
        g = PIGen.gen_direct_graph_er(10, 0.1)
        print(g.get_arch_list())

    def test_u_er_generation(self):
        g = PIGen.gen_indirect_graph_er(10, 0.1)
        print(g.get_arch_list())

    def test_dpa_generation(self):
        g = PIGen.gen_direct_graph_dpa(2, 4)
        print(g.get_arch_list())

    def test_upa_generation(self):
        g = PIGen.gen_indirect_graph_upa(2, 4)
        print(g.get_arch_list())

