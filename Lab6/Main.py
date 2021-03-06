import csv
from math import log

from matplotlib import pyplot as plt

from Lab6.Algorithms import *

with open("unifiedCancerData/unifiedCancerData_896.csv", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    points = list()
    for row in reader:
        points.append(County(int(row[0]), float(row[1]), float(row[2]), int(row[3]), float(row[4])))

    points = list(reversed(sorted(points, key=lambda p: p.population())))

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

    # CHOOSE THE ALGORITHM HERE
    # res = hierarchical_clustering(points, 9)
    res = k_means_clustering(points, 9, 5)

    map_img = plt.imread("map/USA_Counties.png")
    im_plot = plt.imshow(map_img)

    xs = list()
    ys = list()
    ps = list()
    rs = list()
    colours_list = list()
    centroids_list = list()

    i = 0
    for c in res:
        i += 1
        xs += list(map(lambda p: p.x(), c.get_elements()))
        ys += list(map(lambda p: p.y(), c.get_elements()))
        ps += list(map(lambda p: p.population(), c.get_elements()))
        rs += list(map(lambda p: p.risk(), c.get_elements()))
        colours_list += [i for _ in c.get_elements()]
        centroids_list.append(c.get_centroid())

    # Change ps scale
    ps = list(map(lambda p_i: log(p_i) * 3, ps))
    for c in res:
        for e in c.get_elements():
            plt.plot((c.get_centroid().x(), e.x()), (c.get_centroid().y(), e.y()),
                     linestyle='-', c='#FF0000', linewidth=0.5)
    plt.scatter(x=xs, y=ys, s=ps, c=colours_list)
    plt.scatter(x=list(map(lambda c_i: c_i.get_centroid().x(), res)),
                y=list(map(lambda c_i: c_i.get_centroid().y(), res)),
                s=50, marker="*", c="k", zorder=10)

    plt.show()

    print("DIST HIERARCHICAL:", sum(map(lambda cluster: cluster.get_error(), hierarchical_clustering(points, 16))))
    print("DIST K MEANS:", sum(map(lambda cluster: cluster.get_error(), k_means_clustering(points, 16, 5))))

    hierarchical_dist = [sum(map(lambda cluster: cluster.get_error(), hierarchical_clustering(points, i))) for i in
                         range(6, 21)]
    k_means_dist = [sum(map(lambda cluster: cluster.get_error(), k_means_clustering(points, i, 5))) for i in
                    range(6, 21)]

    plt.plot(list(range(6, 21)), hierarchical_dist, c='r')
    plt.plot(list(range(6, 21)), k_means_dist, c='b')
    plt.xlabel("Number of clusters")
    plt.ylabel("Distortion")
    plt.legend(["HierarchicalClustering distortion", "K-Means distortion"])
    plt.title("unifiedCancerData_896")
    plt.show()
