

class Cluster:
    def __init__(self, elem):
        """
        :param: elements:
        """
        self._elements = elem  # array of tuple of points (xi,yi)
        self._centroid = self.calculate_centroid()