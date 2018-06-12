
def HierarchicalClustering(p, k):
    n = len(p)
    insieme = set()
    for point in p:
        node = set()
        node.add(point)
        insieme.add(node)

    while len(insieme) > k:
        i, j = #invoca fastclosestpair
        i = i.union(j)
        insieme.remove(j)

    return insieme
