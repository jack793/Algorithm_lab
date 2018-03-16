import unittest

from _PIGraph import PIDirectGraph


class TestAppendAndData(unittest.TestCase):
    def test_append_and_data(self):
        g = PIDirectGraph()
        g.append(1, 2)
        g.append(1, 3)
        g.append(1, 3)

        self.assertEqual(g.adj_list(), {(1, 2), (1, 3)})


class TestRemove(unittest.TestCase):
    def test_remove(self):
        g = PIDirectGraph()
        g.append(1, 2)
        g.append(1, 3)
        g.append(1, 3)

        g.remove(1, 3)

        self.assertEqual(g.adj_list(), {(1, 2)})


class TestInOutDegree(unittest.TestCase):
    def test_remove(self):
        g = PIDirectGraph()

        g.append(4, 1)
        g.append(5, 1)
        g.append(6, 1)

        g.append(1, 2)
        g.append(1, 3)
        g.append(1, 4)
        g.append(1, 5)

        self.assertEqual(g.in_degree(1), 3)
        self.assertEqual(g.out_degree(1), 4)


if __name__ == '__main__':
    unittest.main()
