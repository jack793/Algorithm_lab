import math

import numpy as np

INFINITY = float('inf')


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

    # print(extraction_list)

    # Add second node
    c.append(min(enumerate(adj_matrix[0, 1:]), key=lambda t: t[1])[0])

    # print(list(enumerate(adj_matrix[0, 1:])))

    not_extracted_nodes.remove(c[1])

    def get_new_k():
        """
        Find new k value to insert in the cycle
        :return: (i,k)
            i - left node index in the list
            k - new node to insert
        """

        res = (-2, -1, math.inf)
        # for node in range(len(c)):
        #     i, j = (c[node], c[(node + 1) % len(c)])
        #     indexes = [k for k in extraction_list]
        #     new_res = node, min(indexes, key=lambda k: adj_matrix[i, k] + adj_matrix[k, j] - adj_matrix[i, j])
        #     res = min(res, new_res, key=lambda v: v[1])
        #     print(adj_matrix[c[res[0]], res[1]] + adj_matrix[c[(res[0] + 1) % len(c)], res[1]])

        indexes = [
            (i, k, j)
            for i, j in map(lambda v: (v, (v + 1) % len(c)), range(len(c)))
            for k in not_extracted_nodes]
        i, k, j = min(indexes,
                      key=lambda tup: adj_matrix[c[tup[0]], tup[1]] + adj_matrix[tup[1], c[tup[2]]] - adj_matrix[
                          c[tup[0]], c[tup[2]]])

        dist = adj_matrix[c[i], k] + adj_matrix[k, c[j]] - adj_matrix[c[i], c[j]]

        res = min(res, (i, k, dist), key=lambda v: v[2])

        if res is (-1, 0, math.inf):
            raise Exception("No node found in the extraction list")

        return res

    while not_extracted_nodes:
        precedent_node_index, new_node, new_dist = get_new_k()
        not_extracted_nodes.remove(new_node)
        c.insert(precedent_node_index + 1, new_node)

    for v in list(map(lambda v: (c[v], c[(v + 1) % len(c)], adj_matrix[v, (v + 1) % len(c)]), range(len(c)))):
        print(v)
    return sum(map(lambda v: adj_matrix[v, (v + 1) % len(c)], range(len(c))))
