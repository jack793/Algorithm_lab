from Lab6.Cluster import *


def hierarchical_clustering(p, k):
    insieme = set()
    for point in p:
        c = Cluster({point})
        insieme.add(c)

    while len(insieme) > k:
        i, j =  # fastclosest_pair
        i = i.union(j)
        insieme.remove(j)

    return insieme
