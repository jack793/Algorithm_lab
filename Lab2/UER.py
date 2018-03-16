from random import random


def gen_direct_tree(n, p):
    data = dict()
    for u in range(0, n):
        data[u] = set()
        for v in range(0, n):
            a = random()
            if a < p:
                data[u].add(v)
    return data


def gen_indirect_tree(n, p):
    data = dict()
    for u in range(0, n):
        data[u] = set()
        for v in range(0, n):
            a = random()
            if a < p:
                data[v] = set()

                data[u].add(v)
                data[v].add(u)
    return data


