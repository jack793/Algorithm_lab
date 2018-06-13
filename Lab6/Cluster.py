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
        self._centroid = None  # variable that contains the Point of the centroid
        self._error = None  # variable that contains the error of the cluster

        self._centroid_cached = False
        self._error_cached = False

    def add_point(self, point):
        self._elements.add(point)
        self._calculate_centroid()

    def get_elements(self):
        """
        Returns the set of points of the cluster
        :return:
        """
        return self._elements

    def get_centroid(self):
        """
        Returns the Point of the centroid, result is cached.
        :return:
        """
        if not self._centroid_cached:
            self._calculate_centroid()
        return self._centroid

    def get_error(self) -> float:
        """
        Returns the error of the cluster, result is cached.
        Error defined as square of the sum of the distances from each point of the cluster to its centroid.
        :return: error
        """
        if not self._error_cached:
            self._calculate_error()
        return self._error

    def union(self, cluster) -> None:
        """
        Merge the cluster with another one.
        :param cluster:
        :return: None
        """
        self._elements = self._elements.union(cluster.get_elements())
        self._calculate_centroid()

    def _calculate_centroid(self):
        """
        Calculates the centroid of the cluster and updates the cache status
        """

        sum_x = 0
        sum_y = 0

        for i in self._elements:
            sum_x += i.x()
            sum_y += i.y()

        self._centroid = Point(sum_x / len(self._elements), sum_y / len(self._elements))
        self._centroid_cached = True

    def _calculate_error(self):
        """
        Calculates the error of the cluster and updates the cache.
        Error defined as square of the sum of the distances from each point of the cluster to its centroid.
        :return: error
        """
        self._error = sum(map(lambda p: pow(Point.distance(p, self.get_centroid()), 2), self._elements))
        self._error_cached = True
