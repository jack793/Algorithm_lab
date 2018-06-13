class Point(object):
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

    @staticmethod
    def distance(p1, p2):
        return pow(pow(p1.x() - p2.x(), 2) + pow(p1.y() - p2.y(), 2), 1 / 2)


class County(Point):

    def __init__(self, c, x, y, p, r) -> None:
        """

        :param c: County Code
        :param x: Coord x
        :param y: Coord y
        :param p: Population
        :param r: Risk of Cancer
        """
        super().__init__(x, y)
        self._code = c
        self._pop = p
        self._risk = r

    def code(self):
        return self._code

    def population(self):
        return self._pop

    def risk(self):
        return self._risk

    def __repr__(self):
        return "(" + str(self._code) + ", " + str(self._x) + ", " + str(self._y) + ", " + str(self._pop) + ", " + str(self._risk) + ")\n"

