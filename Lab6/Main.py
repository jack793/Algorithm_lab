from matplotlib import pyplot as plt, cm
from Lab6.Algorithms import *
import csv

from Lab6.Algorithms import *

with open("unifiedCancerData/unifiedCancerData_111.csv", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    points = set()
    for row in reader:
        points.add(County(int(row[0]), float(row[1]), float(row[2]), int(row[3]), float(row[4])))

    # print(hierarchical_clustering(points, 15))
    # print(k_means_clustering(points, 15, 100))
    #
    # map_img = plt.imread("map/USA_Counties.png")
    # im_plot = plt.imshow(map_img)
    #
    # xs = list()
    # ys = list()
    # ps = list()
    # rs = list()
    #
    # for row in reader:
    #     xs.append(float(row[1]))
    #     ys.append(float(row[2]))
    #     ps.append(log(float(row[3])) / 5)
    #     rs.append(float(row[4]))
    #
    # plt.scatter(x=xs, y=ys, s=ps, c=linspace(0, 1000, 3108))
    # plt.show()
    #
    # # print(hierarchical_clustering(points, 15))
    # # print(k_means_clustering(points, 15, 100))