from math import log

from matplotlib import pyplot as plt, cm
from numpy import linspace

from Lab6.Algorithms import *
import csv

from Lab6.Algorithms import *

with open("unifiedCancerData/unifiedCancerData_111.csv", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    points = set()
    # for row in reader:
    #     points.add(County(int(row[0]), float(row[1]), float(row[2]), int(row[3]), float(row[4])))
    #
    # print(hierarchical_clustering(points, 15))
    # print(k_means_clustering(points, 15, 100))

    # On-screen, things will be displayed at 80dpi regardless of what we set here
    # This is effectively the dpi for the saved figure. We need to specify it,
    # otherwise `savefig` will pick a default dpi based on your local configuration
    dpi = 95

    im_data = plt.imread('map/USA_Counties.png')
    height, width, nbands = im_data.shape

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, interpolation='nearest')

    # Ensure we're displaying with square pixels and the right extent.
    # This is optional if you haven't called `plot` or anything else that might
    # change the limits/aspect.  We don't need this step in this case.
    ax.set(xlim=[0, width], ylim=[height, 0], aspect=1)

    xs = list()
    ys = list()
    ps = list()
    rs = list()

    for row in reader:
        xs.append(float(row[1]))
        ys.append(float(row[2]))
        ps.append(log(float(row[3])) / 5)
        rs.append(float(row[4]))

    plt.scatter(x=xs, y=ys, s=ps)
    # fig.savefig('graph.png', dpi=dpi, transparent=True)
    plt.show()


    # print(hierarchical_clustering(points, 15))
    # print(k_means_clustering(points, 15, 100))