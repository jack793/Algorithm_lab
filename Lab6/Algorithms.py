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


def slow_closest_pair(p: [Point]):
    """
    Returns the indexes of the two closest clusters and the distance between the two
    :param p - list of Points
    :return: (i1, i2, d) - where i1 and i2 are the indexes of the two points and d is the distance between them
    """
    tuples = {(i1, i2) for i1 in range(len(p)) for i2 in range(len(p)) if i1 is not i2}
    i1, i2 = min(tuples, key=lambda t: Point.distance(p[t[0]], p[t[1]]))
    return i1, i2, Point.distance(p[i1], p[i2])


def fast_closest_pair(p, s):
    n = len(p)
    if n <= 3:
        return slow_closest_pair(p)

def split(s,pl):
    n = len(s)
    sl = list()
    sr = list()
    j = 0
    k = 0
    for i in range(0,n):
        for q in pl:
            if s[i] is pl[q]:
                sl[j] = s[i]
                j = j+1
            else:
                sr[k] = s[i]
                k = k+1

    return sl, sr