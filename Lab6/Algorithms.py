
from Lab6.Cluster import *

def HierarchicalClustering(p, k):
    insieme = set()
    for point in p:
        c = Cluster(point)
        insieme.add(c)

    while len(insieme) > k:
        i, j = #invoca fastclosestpair
        i = i.union(j)
        insieme.remove(j)

    return insieme
