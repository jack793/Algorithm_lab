from math import inf, floor

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


def slow_closest_pair(p):
    min_distance = inf
    nearest_points = None  # tuple (i,j) point coordinates

    for pu, i in enumerate(p):
        for pv, j in enumerate(p):
            if pv > pu:
                distance = Point.distance(i.x, j.x)
                if distance < min_distance:  # smaller distance between pairs of points (i,j)
                    min_distance = distance
                    nearest_points = (i, j)

    return min_distance, nearest_points.x, nearest_points.y


def fast_closest_pair(p, s):
    n = len(p)
    if n <= 3:
        return slow_closest_pair(p)
