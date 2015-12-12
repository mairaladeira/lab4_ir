import networkx as nx
import matplotlib.pyplot as plt
import time
import math
__author__ = 'Gabriela and Maira'


def get_er_graph(n, p):
    """
    Function to get an ER graph
    :param n: number of nodes
    :param p: probability of connection between the nodes
    :return: ER graph
    """
    return nx.fast_gnp_random_graph(n, p)


def get_ws_graph(n, p):
    """
    Function to get a WS graph with 4 k-nearest-neighbors
    :param n: number of nodes
    :param p: probability of connection between the nodes
    :return: WS graph
    """
    return nx.watts_strogatz_graph(n, 4, p)


def get_shortest_path_average_len(g):
    """
    returns the average shortest path length of a graph
    :param g: ER or WS graph
    :return: average shortest path len
    """
    sps = nx.shortest_path_length(g)
    paths_size = 0
    for n0 in sps.values():
        for n1 in n0.values():
            paths_size += n1
    n_nodes = g.number_of_nodes()
    return paths_size/float(n_nodes*(n_nodes-1))


def get_clustering_coefficient(g):
    """
    returns the clustering coefficient of a graph
    :param g: ER or WS graph
    :return: clustering coefficient path len
    """
    return nx.average_clustering(g)


def get_p_for_connected_graph(n):
    """
    get the appropriated probability for a ER graph according to the number of the nodes of the graph
    :param n: number of nodes
    :return: appropriated probability
    """
    e = 0.0005
    p = (((1 + e)*math.log(n))/n)*1.1
    return p


def task1():
    """
    Task 1 of the laboratory 4
    """
    g = get_ws_graph(1000, p=0)
    spa_0 = get_shortest_path_average_len(g)
    cc_0 = get_clustering_coefficient(g)
    spa = []
    cc = []
    p = [0.0001, 0.0003, 0.0005, 0.0007, 0.0009, 0.002, 0.004, 0.006,
         0.008, 0.01, 0.03, 0.05, 0.07, 0.09, 0.2, 0.4, 0.6, 0.8, 1]
    p_lables = [0.0001, 0.001, 0.01, 0.1, 1]
    for i in p:
        g = get_ws_graph(1000, i)
        spa.append(get_shortest_path_average_len(g)/spa_0)
        cc.append(get_clustering_coefficient(g)/cc_0)
    print(spa)
    print(cc)
    plt.plot(p, spa, 'ko', label="ASP")
    plt.hold(1)
    plt.plot(p, cc, 'ws', alpha=0.7, label="CC")
    plt.xticks(p_lables)
    plt.xscale('log')
    xx, locs = plt.xticks()
    ll = ['%.4f' % a for a in xx]
    plt.xticks(xx, ll)
    plt.axis([-0.5, 1.05, -0.05, 1.05])
    plt.legend(loc=(0.5, 0.5), numpoints=1)
    plt.show()


def task2():
    """
    Task 2 of the laboratory 4
    """
    ns = [5, 50, 110, 300, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
    p_lables = [5, 500, 1000, 5000, 10000]
    asp = []
    for n in ns:
        p = get_p_for_connected_graph(n)
        g = get_er_graph(n, p)

        sp = get_shortest_path_average_len(g)
        asp.append(sp)
        print(str(p) + ": " + str(sp))
    print(asp)
    plt.plot(ns, asp, 'ko', linestyle='--', label="Average Shortest Path")
    plt.xticks(p_lables)
    #plt.xscale('exp')
    plt.axis([-100, 11000, 0, 4])
    plt.legend(loc=(0.5, 0.2), numpoints=1)
    plt.show()
    return

start_time = time.time()
task1()
task2()
print("--- %s seconds ---" % (time.time() - start_time))