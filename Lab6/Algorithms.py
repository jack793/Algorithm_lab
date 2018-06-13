from math import inf, floor

from Lab6.Cluster import *
from Lab6.Point import *


def hierarchical_clustering(p: {Point}, k: int):
    """
    hierarchical_clustering algorithm
    :param p: set of Points from data
    :param k: number of required clusters
    :return: a set containing the required number of clusters
    """
    cluster_set = set()
    for point in p:
        c = Cluster({point})
        cluster_set.add(c)

    while len(cluster_set) > k:
        centroids = {c.get_centroid(): c for c in cluster_set}
        _, i, j = fast_closest_pair(
            list(sorted(centroids.keys(), key=lambda p_i: p_i.x())),
            list(sorted(centroids.keys(), key=lambda p_i: p_i.y())))

        ci, cj = centroids[i], centroids[j]
        ci.union(cj)
        cluster_set.remove(cj)

    return cluster_set


def k_means_clustering(p: {Point}, k: int, q: int):
    """
    K means clustering algorithm
    :param p: set of Points
    :param k: number of required clusters
    :param q: number of iterations
    :return: cluster_set from p
    """
    n = len(p)

    # creating k centers
    centers = [p[i][0] for i in range(k)]

    cluster_set = []

    # INITIALIZATION: creating k empty cluster
    for i in range(q):
        cluster_set = [Cluster(set()) for _ in range(k)]

        # ASSIGNMENT: finally, add current point to the best cluster
        for j in range(n):
            # for each point..
            min_d = inf
            closest_c = None
            for c in range(k):
                # ..searching for closest center to current point
                d = Point.distance(centers[c], p[j])
                if d < min_d:
                    min_d = d
                    closest_c = c

            cluster_set[closest_c].add_point(p[j])

        # UPDATE: recalculating cluster_set centroids for next iteration
        for f in range(k):
            if cluster_set[f].get_centroid() is not None:
                centers[f] = cluster_set[f].get_centroid()

    return cluster_set


def slow_closest_pair(p: [Point]):
    """
    Returns the indexes of the two closest clusters and the distance between the two
    :param p - list of Points
    :return: (d, i1, i2) - where d is the distance between them and i1 and i2 are the indexes of the two points
    """
    tuples = {(p1, p2) for p1 in p for p2 in p if p1 is not p2}
    p1, p2 = min(tuples, key=lambda t: Point.distance(t[0], t[1]))
    return Point.distance(p1, p2), p1, p2


def fast_closest_pair(p, s):
    """
    :param p: vector containing Points ordered by x coordinate
    :param s: vector containing Points ordered by y coordinate
    :return: (d, i, j) tuple where d is the smallest distance btw couple of points in s in vertical strip [mid-d, mid+d]
        and i,j are the two points
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
        (d, pi, pj) = min(fast_closest_pair(pl, sl), fast_closest_pair(pr, sr))

        x1 = (p[m - 1]).x()
        x2 = (p[m]).x()
        mid = (x1 + x2) / 2

        return min((d, pi, pj), closest_pair_strip(s, mid, d))


def split(s: [Point], pl: [Point]):
    """
    Split the s vector in sl and sr
    :param s: vector in which points are ordered by their y coord
    :param pl: vector in which points are ordered by their x coord, containing only the left part of p
    :return: sl(which contains all points in pl, but ordered by their y coord) and sr(which contains all points in pr, but ordered by their y coord)
    """
    sl = list(filter(lambda s_i: s_i in pl, s))
    sr = list(filter(lambda s_i: s_i not in pl, s))
    return sl, sr


def closest_pair_strip(s: [Point], mid: float, d: float) -> tuple:
    """
    Seek if there are points at the two different extremities of the line mid, which distance is < than d
    :param s: vector in which points are ordered by their y coord
    :param mid: coord x of the vertical line which divide pl from pr
    :param d: minimum of distance between the minimum of distances in pl and those on ps
    :return: (d,i,j) as smallest distance between two points within 1d from mid and the two points
    """
    n = len(s)
    s1 = list(filter(lambda s_i: abs(s_i.x() - mid) < d, s))
    k = len(s1)

    # s1 now contains only the points within 1d from the mid rect on the x axis

    d, i, j = inf, None, None

    # u iterates 0, ... , k - 2
    for u in range(k - 1):
        # v iterates u + 1, ... , min{u + 3, n - 1}
        for v in range(u + 1, min(u + 3, n - 1) + 1):
            if Point.distance(s1[u], s1[v]) < d:
                d, i, j = Point.distance(s1[u], s1[v]), s1[u], s1[v]

    return d, i, j
