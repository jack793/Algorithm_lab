from math import floor

from Lab6.Cluster import *
from Lab6.Point import *


def hierarchical_clustering(p, k):
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
    n = len(p)
    if n <= 3:
        return slow_closest_pair(p)

    else:
        m = floor(n / 2)
        pl = p[0:m]  # left part
        pr = p[m:]  # right part

        sl, sr = split(s, pl)

        (d, i, j) = min(fast_closest_pair(pl, sl), fast_closest_pair(pr, sr))

        x1 = (p[m - 1]).x
        x2 = (p[m]).x
        mid = (x1 + x2) / 2

        return min((d, i, j), closest_pair_strip(s, mid, d))


def split(s, pl):
    sl = list()
    sr = list()

    for s_i in s:
        if s_i in pl:
            sl.append(s[s_i])
        else:
            sr.append(s[s_i])

    return sl, sr


def closest_pair_strip(s, mid, d) -> tuple:
    n = len(s)
    s1 = list()
    k = 0
    for i in range(0, n):
        if abs(s[i].x - mid) < d:
            s1[k] = s[i]
            k = k+1

    d = inf
    i = -1
    j = -1
    for u in range(0, k-1):
        for v in range(u+1, min(u+3, n-1)):
            if Point.distance(u, v) < d:
                d = Point.distance(u, v)
                i = u
                j = v

    return d, i, j

