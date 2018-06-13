from math import inf, floor

from Lab6.Cluster import *
from Lab6.Point import *


def hierarchical_clustering(p: {Point}, k: int):
    """
    hierarchical_clustering algorithm
    :param p: set of Points
    :param k: number of required clusters
    :return: a set containing the required number of clusters
    """
    insieme = set()
    for point in p:
        c = Cluster({point})
        insieme.add(c)

    while len(insieme) > k:
        # i, j =  # fastclosest_pair
        # i = i.union(j)
        # insieme.remove(j)
        pass

    return insieme


def k_means_clustering(p: {Point}, k: int, q: int):
    """
    K means clustering algorithm
    :param p: set of Points
    :param k: number of required clusters
    :param q: number of interactions
    :return:
    """
    c = {Cluster({p_i}) for p_i in p}

    # test if the number of clusters is larger than the size of set of points
    if k >= len(p):
        return c

    for iteration in range(q):
        # TODO continue
        pass


def slow_closest_pair(p: [Point]):
    """
    Returns the indexes of the two closest clusters and the distance between the two
    :param p - list of Points
    :return: (d, i1, i2) - where d is the distance between them and i1 and i2 are the indexes of the two points
    """
    tuples = {(i1, i2) for i1 in range(len(p)) for i2 in range(len(p)) if i1 is not i2}
    i1, i2 = min(tuples, key=lambda t: Point.distance(p[t[0]], p[t[1]]))
    return Point.distance(p[i1], p[i2]), i1, i2


def fast_closest_pair(p, s):
    """

    :param p: clusters
    :param s: vector contains indexes of points ordered by y coordinate
    :return: (d, i, j) tuple where d is the smallest distance btw couple of points in s in vertical strip [mid-d, mid+d]
        and i,j indexes of this two points
    """
    n = len(p)
    if n <= 3:
        return slow_closest_pair(p)

    else:
        m = floor(n / 2)
        pl = p[0:m]  # left part
        pr = p[m:]  # right part

        sl, sr = split(s, pl)

        # fast_closest_pair returns a tuple, min checks first the distance
        (d, i, j) = min(fast_closest_pair(pl, sl), fast_closest_pair(pr, sr))

        x1 = (p[m - 1]).x
        x2 = (p[m]).x
        mid = (x1 + x2) / 2

        return min((d, i, j), closest_pair_strip(s, mid, d))


def split(s: [Point], pl: [Point]):
    """
    Split the s vector in sl and sr
    :param s: vector in which points are ordered by their y coord
    :param pl: vector in which points are ordered by their x coord, containing only the left part of p
    :return: sl(which contains all points in pl, but ordered by their y coord) and sr(which contains all points in pr, but ordered by their y coord)
    """
    sl = filter(lambda s_i: s_i in pl, s)
    sr = filter(lambda s_i: s_i not in pl, s)
    return sl, sr


def closest_pair_strip(s: [Point], mid: float, d: float) -> tuple:
    """
    Seek if there are points at the two different extremities of the line mid, which distance is < than d
    :param s: vector in which points are ordered by their y coord
    :param mid: coord x of the vertical line which divide pl from pr
    :param d: minimum of distance between the minimum of distances in pl and those on ps
    :return: (d,i,j) as smallest distance between two points within 1d from mid and the two points indexes
    """
    n = len(s)
    s1 = list()
    for s_i in s:
        if abs(s_i.x - mid) < d:
            s1.append(s_i)
    k = len(s1)

    # s1 now contains only the points within 1d from the mid rect on the x axis

    d, i, j = inf, -1, -1

    # u iterates 0, ... , k - 2
    for u in range(k - 1):
        # v iterates u + 1, ... , min{u + 3, n - 1}
        for v in range(u + 1, min(u + 3, n - 1)):
            if Point.distance(u, v) < d:
                d = Point.distance(u, v)
                i = u
                j = v

    return d, i, j
