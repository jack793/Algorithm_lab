import numpy as np
from math import cos, acos, sqrt

# global
PI = 3.141592
RRR = 6378.388
INFINITY = float('inf')


class Graph:
    def __init__(self, input_data, is_geo=False):  # geo is False
        # init adj_matrix w/ all 0 values
        self._length = len(input_data)
        self._adj_matrix = np.zeros((self._length, self._length), dtype=int)  # A data data_type object (using numpy)

        self._create_adj_matrix(input_data, is_geo)
        self._distances = {}  # distance dict key its a tuple (v, s)
        self._predecessors = {}  # again a tuple key

    def _create_adj_matrix(self, input_data, is_geo):  # format, pass data_type o euc format
        for i in input_data:
            for j in input_data:
                if i[0] != j[0]:
                    # geo = False
                    # None if i == j
                    self._adj_matrix[int(i[0]) - 1][int(j[0]) - 1] = Graph.calc_distance(i, j, is_geo)

    def get_distances(self, key):
        """

        :param key: is a tuple
        :return: distance (x,y) y to x
        """
        try:
            return self._distances[key]
        except KeyError:
            return None

    def set_distances(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        self._distances[key] = value

    def get_parents(self, key):
        return self._predecessors[key]

    def get_adj_matrix(self, u=None, v=None):
        if u is None or v is None:
            return self._adj_matrix
        else:
            return self._adj_matrix[u, v]

    def get_len(self):
        return self._length

    def set_parents(self, key, value):
        self._predecessors[key] = value

    @staticmethod
    def convert_to_rads(val):
        deg = int(val)
        min_ = val - deg
        rad = PI * (deg + 5.0 * min_ / 3.0) / 180.0

        return rad

    @staticmethod
    def calc_distance(i, j, is_geo: bool):
        if is_geo:
            lat_i = Graph.convert_to_rads(i[1])  # u[0] index,  u[1] u[2] node latitude, longitude
            long_i = Graph.convert_to_rads(i[2])

            lat_j = Graph.convert_to_rads(j[1])
            long_j = Graph.convert_to_rads(j[2])

            q1 = cos(long_i - long_j)
            q2 = cos(lat_i - lat_j)
            q3 = cos(lat_i + lat_j)
            dij = int(RRR * acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0)
        else:
            dij = int(sqrt((i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2))
        return dij
