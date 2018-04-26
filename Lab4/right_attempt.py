from Lab4.algorithms import *
from Lab4.graph import *

geo = False
cont = 1
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

# print(dataset[0].split(":")[1])
# print(dataset)
data_length = len(dataset)
s = tuple(np.arange(data_length))
# create_adj_matrix(n)
# adj_matrix = create_adj_matrix(dataset)

graph = Graph(dataset, geo)
# print("matrix: \n", graph.get_adj_matrix())
print(held_karp(graph, 0, s))
