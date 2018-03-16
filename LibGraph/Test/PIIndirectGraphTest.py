import unittest

from LibGraph.PIGraph import PIIndirectGraph


class TestAppendAndData(unittest.TestCase):
    def test_append_and_data(self):
        g = PIIndirectGraph()
        g.append(1, 2)
        g.append(1, 3)
        g.append(1, 3)

        self.assertEqual(g.adj_list(), {(1, 2), (1, 3)})


class TestRemove(unittest.TestCase):
    def test_remove(self):
        g = PIIndirectGraph()
        g.append(1, 2)
        g.append(1, 3)
        g.append(1, 3)

        g.remove(1, 3)

        self.assertEqual(g.adj_list(), {(1, 2)})


class TestInOutDegree(unittest.TestCase):
    def test_remove(self):
        g = PIIndirectGraph()

        g.append(4, 1)
        g.append(5, 1)
        g.append(6, 1)

        g.append(1, 2)
        g.append(1, 3)
        g.append(1, 4)
        g.append(1, 5)

        self.assertEqual(g.degree(1), 5)


if __name__ == '__main__':
    unittest.main()
