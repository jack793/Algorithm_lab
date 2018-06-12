class Cluster(object):
    """
    Management class for cluster
    """
    def __init__(self, elements: set):
        """
        :param: elements: set of points to insert in the cluster
        """
        self._elements = elements  # array of tuple of points (xi,yi)
        self._centroid = self.calculate_centroid()

    def calculate_centroid(self):
        """
        function that returns the cluster's centroid
        """

        return self._centroid

    def get_points(self):
        return self._elements

    def get_centroid(self):
        return self._centroid

    def union(self, cluster: Cluster) -> None:
        self._elements = self._elements.union(cluster.get_points())
        self._centroid = self.calculate_centroid()
