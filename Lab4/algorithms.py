import math
import numpy as np


def held_karp(graph, v, s):
    """
    :param graph: Graph
    :param v: target node
    :param s: list of nodes (s its considered like a dict)
    :return: cost of the min path from 0 to v that visit all nodes in s
    """
    # base case
    if len(s) == 1:
        # print("base case:", v)
        return graph.get_adj_matrix(v, 0)  # s have only 1 element
    elif graph.get_distances((v, s)) is not None:
        return graph.get_distances((v, s))
    else:
        min_dist = math.inf
        min_prec = None
        s1 = tuple([u for u in s if u != v])
        for u in s1:
            dist = held_karp(graph, u, s1)  # recursive call
            # print("dist:", dist)
            # print("currently arch:", graph.get_adj_matrix(u, v))
            # print("comparison:", dist + graph.get_adj_matrix(u, v), min_dist)
            if dist + graph.get_adj_matrix(u, v) < min_dist:  # update like algorithm says to me
                min_dist = dist + graph.get_adj_matrix(u, v)
                min_prec = u
        graph.set_distances((v, s), min_dist)
        graph.set_parents((v, s), min_prec)
        return min_dist


def get_cycle_cost(graph, cycle):
    adj_matrix = graph.get_adj_matrix()
    cost = 0
    length = len(cycle)
    for i in range(length):
        j = i + 1
        if j == length:
            # out of bounds
            j = 0
        cost += adj_matrix[cycle[i]][cycle[j]]

    return cost


#       METHOD OF CHEAPEST INSERTION
# 1. Choose an arbitrary node i as a starting node.
# 2. Find a node j closest to i. Form a subtour T = i-j-i.
# 3. Find an edge [i,j] of the subtour and a node k not in the subtour, such that the increase of
# length f = c + c - c is minimized. Modify the subtour by inserting k between i and j. ik kj ij
# 4. Go to 3 until a Hamiltonian cycle is formed.

def cheapest_insertion(graph):
    """
    :param graph: a weighted graph G = (V, E)
    :return: cost of the Hamiltonian cycle
    """
    # (1) Initialization:
    # Consider the partial circuit composed only of the vertex 0. Find a
    # vertex j that minimizes w (0, j) and constructs the partial circuit (0, j);

    c = [0]
    adj_matrix = graph.get_adj_matrix()

    not_extracted_nodes = set(np.arange(graph.get_len()))
    not_extracted_nodes.remove(0)

    # Add second node
    c.append(min(enumerate(adj_matrix[0, 1:]), key=lambda t: t[1])[0])

    not_extracted_nodes.remove(c[1])

    # (2) Selection:
    def cheapest_selection(not_extracted, cy):
        min_value = math.inf
        edge = None
        next_node = None
        for i, node in enumerate(cy):
            # for all k (nodes) not yet extracted we search for a k and a edge(_,_) that min the cycle cost
            for node_k in not_extracted:
                j = i + 1
                if j == len(cy):
                    # if out of bound w/ y, finished the hcycle
                    j = 0

                if adj_matrix[cy[i]][node_k] + adj_matrix[cy[j]][node_k] - adj_matrix[cy[i]][cy[j]] < min_value:
                    min_value = adj_matrix[cy[i]][node_k] + adj_matrix[cy[j]][node_k] - adj_matrix[cy[i]][cy[j]]
                    edge = (i, j)
                    next_node = node_k

        return edge, next_node

    while not_extracted_nodes:

        edges, k = cheapest_selection(not_extracted_nodes, c)

        not_extracted_nodes.remove(k)

        # (3) Insertion:
        # connect last node w/ the 1st
        if edges[1] == 0:
            c.append(k)
        else:
            c.insert(edges[1], k)

    return get_cycle_cost(graph, c)
