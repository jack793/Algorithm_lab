from Lab4.algorithms import *
from Lab4.graph import *

geo = False
cont = 1
# input_name = "Data/berlin52.tsp"
input_name = "Lab4/Data/berlin52.tsp"

with open(input_name) as f:
    line = f.readline()
    while line != "NODE_COORD_SECTION\n":
        if "EDGE_WEIGHT_TYPE" in line:
            if line.split(":")[1] == " GEO\n":
                geo = True

        line = f.readline()
        cont += 1

dataset = np.loadtxt(input_name, skiprows=cont, comments=["EOF"])

# print(dataset)
# data_length = len(dataset)
# s = tuple(np.arange(data_length))
#
# graph1 = Graph(dataset, geo)
# print("matrix: \n", graph1.get_adj_matrix())
# print(held_karp(graph1, 0, s))

# cheapest_insertion(graph)

graph2 = Graph(dataset, geo)
print(cheapest_insertion(graph2))
