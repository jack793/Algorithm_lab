from Lab6.Point import Point


class Cluster(object):
    """
    Management class for cluster
    """

    def __init__(self, elements: set):
        """
        :param: elements: set of points to insert in the cluster
        """
        assert len(elements) > 0
        self._elements = elements  # array of tuple of points (xi,yi)
        self._centroid = self.calculate_centroid()  # function that calculated the centroid

    def calculate_centroid(self):
        """
        function that returns the cluster's centroid
        """

        sum_x = 0
        sum_y = 0

        for i in self._elements:
            sum_x += i.x
            sum_y += i.y

        return Point(sum_x / len(self._elements), sum_y / len(self._elements))

    def get_elements(self):
        return self._elements

    def get_centroid(self):
        return self._centroid

    def union(self, cluster) -> None:
        self._elements = self._elements.union(cluster.get_elements())
        self.calculate_centroid()
