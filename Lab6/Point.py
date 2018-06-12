class Point:
    def __init__(self, x, y) -> None:
        super().__init__()
        self._x = x
        self._y = y

    def to_tuple(self) -> tuple:
        """
        Returns a tuple with the point coordinates
        :return:
        """
        return self._x, self._y

    @staticmethod
    def to_point(t: tuple):
        """
        Tuple of two coordinates to a Point
        :param t: (x,y) tuple
        :return:
        """
        assert len(t) == 2
        return Point(t[0], t[1])

    def x(self):
        return self._x

    def y(self):
        return self._y