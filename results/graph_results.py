#!/usr/bin/python3

import matplotlib.pyplot as plt


def read_results():
    n_nodes, n_gflops = [], []
    with open("results.txt") as ifile:
        lines = ifile.readlines()
        for line in lines:
            words = line.split()
            n_nodes.append(int(words[0]))
            n_gflops.append(float(words[1]))
    return n_nodes, n_gflops


def plot_results(n_nodes, n_gflops):
    plt.title("Best GFLOPS achieved against nodes used.")
    plt.xlabel("Number of nodes")
    plt.ylabel("GFLOPS")
    plt.plot(n_nodes, n_gflops, '-o')
    plt.show()


def main():
    n_nodes, n_gflops = read_results()
    plot_results(n_nodes, n_gflops)


if __name__ == "__main__":
    main()