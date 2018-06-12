"""
Management class for cluster
"""


class Cluster:
    def __init__(self, elements):
        """
        :param: elements: array of elements need for initialization
        """
        self._elements = elements  # array of tuple of points (xi,yi)
        self._centroid = self.calculate_centroid()

    def calculate_centroid(self):
        """
        function that returns the cluster's centroid
        """

        return self._centroid
