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
        #TODO continue
        pass

