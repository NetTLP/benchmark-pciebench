#!/usr/bin/env python3

import argparse
import statistics
import matplotlib.pyplot as plt
import matplotlib
from myplotlib import get_marker, get_color, change_aspect_ratio

ratio = 1.5

fontsize = 22
lfontsize = 18
markersize = 11
linewidth = 2.4
lines = { "linewidth" : linewidth,
          "markersize" : markersize,
          "markeredgewidth" : linewidth, }
markers = { "fillstyle" : "none", }
plt.rc("lines", **lines)
plt.rc("markers", **markers)
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42


def parse(filename):
    
    gbpses = []

    with open(filename, "r") as f:
        for line in f:
            gbpses.append(float(line.strip().split(",")[3]))

    return statistics.mean(gbpses)


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern", help = "access pattern",
                        choices = ["fix", "random"], default = "fix")
    parser.add_argument("-r", "--ratio", help = "graph ratio",
                        type = float, default = ratio)
    args = parser.parse_args()

    pdffile = "graph/graph_bw2_{}.pdf".format(args.pattern)

    fig, ax = plt.subplots()

    xticks = []
    yaxis = []

    for x in range(1, 129):

        dma_len = x * 16

        xticks.append(dma_len)
        f = ("output/pciebench_bw2_read_ptr-{}_len-{}.txt".format(args.pattern,
                                                                  dma_len))
        yaxis.append(parse(f))

    ax.plot(xticks, yaxis, color = get_color())
    
    plt.yticks([0, 1, 2, 3, 4, 5])
    plt.xticks([16, 512, 1024, 1536, 2048])

    ax.tick_params(labelsize = fontsize)
    ax.set_ylabel("throughput (Gbps)", fontsize = fontsize)
    ax.set_xlabel("request size (byte)", fontsize = fontsize)
    
    ax.grid(True, linestyle = "--", linewidth = 0.5)

    change_aspect_ratio(ax, args.ratio)

    print("save '{}'".format(pdffile))
    plt.savefig(pdffile, bbox_inches = "tight", pad_inches = 0.005)

if __name__ == "__main__":
    main()
