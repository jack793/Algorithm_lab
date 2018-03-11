from random import random


def gen_direct_tree(nodes, threshold):
    data = dict()
    for u in range(0, nodes):
        data[u] = set()
        for v in range(0, nodes):
            a = random()
            if a < threshold:
                data[u].add(v)
    return data


def gen_indirect_tree(nodes, threshold):
    data = dict()
    for u in range(0, nodes):
        data[u] = set()
        for v in range(0, nodes):
            a = random()
            if a < threshold:
                data[u].add(v)
                data[v].add(u)
    return data


