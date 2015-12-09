import networkx as nx
import matplotlib.pyplot as plt
import time
import math
__author__ = 'Gabriela and Maira'


def get_er_graph(n, p):
    return nx.erdos_renyi_graph(n, p)


def get_ws_graph(n, p):
    return nx.watts_strogatz_graph(n, 4, p, seed=None)


def get_shortest_path_average_len(g):
    sps = nx.shortest_path_length(g)
    paths_size = 0
    for n0 in sps.values():
        for n1 in n0.values():
            paths_size += n1
    n_nodes = g.number_of_nodes()
    return paths_size/float(n_nodes*(n_nodes-1))


def get_clustering_coefficient(g):
    return nx.average_clustering(g)


def get_p_for_connected_graph(n):
    e = 0.0005
    p = (((1 + e)*math.log(n))/n)*1.2
    return p

def task1():
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
    ns = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 200, 250, 300, 350, 500, 1000, 5000, 10000, 200000, 500000]
    p_lables = [10, 100, 500, 1000, 10000, 200000, 600000]
    asp = []
    for n in ns:
        p = get_p_for_connected_graph(n)
        g = get_er_graph(n, p)
        sp = get_shortest_path_average_len(g)
        asp.append(sp)
        print(sp)
    print(asp)
    plt.plot(ns, asp, 'ko', label="ASP")
    plt.xticks(p_lables)
    plt.axis([0, 600010, 0, 25])
    plt.legend(loc=(0.5, 0.5), numpoints=1)
    plt.show()
    return

start_time = time.time()
#task1()
task2()
print("--- %s seconds ---" % (time.time() - start_time))