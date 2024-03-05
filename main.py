import random

import RandomGraphGenerator
from Dijkstra_v1 import Dijkstra_BW_v1
from Dijkstra_v2 import Dijkstra_BW_v2
from Kruskal import Kruskal
from Kruskal_Improved import Kruskal_Improved
import time

graph_count = 1

def run_algos(G, src, dest, printBWPath=False):
    start_time = time.time()
    path1, b_width1 = Dijkstra_BW_v1(G, src, dest)
    dijkstra_BW_v1_time = time.time() - start_time

    start_time = time.time()
    path2, b_width2 = Dijkstra_BW_v2(G, src, dest)
    dijkstra_BW_v2_time = time.time() - start_time

    start_time = time.time()
    kruskal = Kruskal()
    path4, b_width4 = kruskal.Kruskal_BW(G, src, dest)
    kruskal_BW_time = time.time() - start_time

    start_time = time.time()
    kruskal_improved = Kruskal_Improved()
    path4, b_width4 = kruskal_improved.Kruskal_BW(G, src, dest)
    kruskal_improved_BW_time = time.time() - start_time

    if printBWPath:
        print("Dijkstra V1 Bandwidth Path : ", path1)
        print("Dijkstra V2 Bandwidth Path : ", path2)
        print("Kruskal Bandwidth Path : ", path4)
        print("Kruskal_Improved Bandwidth Path : ", path4)
        print("Dijkstra V1 Bandwidth Value : ", b_width1)
        print("Dijkstra V2 Bandwidth Value : ", b_width2)
        print("Kruskal_Improved Bandwidth Value : ", b_width4)
        print("Kruskal Bandwidth Value : ", b_width4)
    assert (b_width1 == b_width2 and b_width1 == b_width4 and b_width1 == b_width4)

    return dijkstra_BW_v1_time, dijkstra_BW_v2_time, kruskal_BW_time, kruskal_improved_BW_time


def testing():
    n = 5000
    G2 = RandomGraphGenerator.generate_graph(2, n)
    src = random.randint(0, n - 1)
    dest = random.randint(0, n - 1)
    kruskal = Kruskal()
    path4, b_width4 = kruskal.Kruskal_BW(G2, src, dest)
    exit(0)


if __name__ == "__main__":
    # testing()
    num_pairs_of_graphs = 5
    num_src_dests = 5
    n = 1000

    algorithm_averages_G1 = [0] * 4  # size 4, average of all 25 tests. 0 - Dijkstra V1, 1 - Dijkstra V2, 2 - Kruskal, 3 - Kruskal Improved
    algorithm_averages_G2 = [0] * 4  # size 4, average of all 25 tests. 0 - Dijkstra V1, 1 - Dijkstra V2, 2 - Kruskal, 3 - Kruskal Improved
    for i in range(num_pairs_of_graphs):
        G1 = RandomGraphGenerator.generate_graph(1, n)
        G2 = RandomGraphGenerator.generate_graph(2, n)
        graph_averages_G1 = [0] * 4  # size 4, average of all 5 tests on same graph. 0 - Dijkstra V1, 1 - Dijkstra V2, 2 - Kruskal, 3 - Kruskal Improved
        graph_averages_G2 = [0] * 4  # size 4, average of all 5 tests on same graph. 0 - Dijkstra V1, 1 - Dijkstra V2, 2 - Kruskal, 3 - Kruskal Improved
        for j in range(num_src_dests):
            src = random.randint(0, n - 1)
            dest = random.randint(0, n - 1)
            while src == dest:
                dest = random.randint(0, n - 1)

            d1_s_time, d2_s_time, k_s_time, ki_s_time = run_algos(G1, src, dest)
            d1_d_time, d2_d_time, k_d_time, ki_d_time = run_algos(G2, src, dest)
            graph_averages_G1[0] += d1_s_time
            graph_averages_G1[1] += d2_s_time
            graph_averages_G1[2] += k_s_time
            graph_averages_G1[3] += ki_s_time
            graph_averages_G2[0] += d1_d_time
            graph_averages_G2[1] += d2_d_time
            graph_averages_G2[2] += k_d_time
            graph_averages_G2[3] += ki_d_time

        for k in range(4):
            algorithm_averages_G1[k] += graph_averages_G1[k]
            algorithm_averages_G2[k] += graph_averages_G2[k]
            graph_averages_G1[k] /= num_src_dests
            graph_averages_G2[k] /= num_src_dests

        print("Average times for G1_"+str(i+1)+" :")
        print("Dijkstra V1 \t\t Dijkstra V2 \t\t Kruskal \t\t Kruskal Improved")
        print("{:.5f}secs \t\t {:.5f}secs \t\t {:.5f}secs \t\t {:.5f}secs".format(graph_averages_G1[0], graph_averages_G1[1], graph_averages_G1[2], graph_averages_G1[3]))
        print("Average times for G2_"+str(i+1)+" :")
        print("Dijkstra V1 \t\t Dijkstra V2 \t\t Kruskal \t\t Kruskal Improved")
        print("{:.5f}secs \t\t {:.5f}secs \t\t {:.5f}secs \t\t {:.5f}secs".format(graph_averages_G2[0], graph_averages_G2[1], graph_averages_G2[2], graph_averages_G2[3]))

    for k in range(4):
        algorithm_averages_G1[k] /= (num_src_dests * num_pairs_of_graphs)
        algorithm_averages_G2[k] /= (num_src_dests * num_pairs_of_graphs)
    print("\n\n\n")
    print("Overall average times for G1 type graphs : ")
    print("Dijkstra V1 \t\t Dijkstra V2 \t\t Kruskal \t\t Kruskal Improved")
    print("{:.5f}secs \t\t {:.5f}secs \t\t {:.5f}secs \t\t {:.5f}secs".format(algorithm_averages_G1[0], algorithm_averages_G1[1], algorithm_averages_G1[2], algorithm_averages_G1[3]))
    print("Overall average times for G2 type graphs : ")
    print("Dijkstra V1 \t\t Dijkstra V2 \t\t Kruskal \t\t Kruskal Improved")
    print("{:.5f}secs \t\t {:.5f}secs \t\t {:.5f}secs \t\t {:.5f}secs".format(algorithm_averages_G2[0], algorithm_averages_G2[1], algorithm_averages_G2[2], algorithm_averages_G2[3]))

