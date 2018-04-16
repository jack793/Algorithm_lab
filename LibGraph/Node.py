class Node:

    def __init__(self, coord_x, coord_y):
        self._x = coord_x # LATITUDINE
        self._y = coord_y # LONGITUDINE

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y