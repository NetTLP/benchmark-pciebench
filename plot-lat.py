#!/usr/bin/env python3

import argparse
import statistics
import matplotlib.pyplot as plt
import matplotlib
from myplotlib import get_marker, get_color, change_aspect_ratio

ratio = 1.5
fontsize = 14
lfontsize = 13.5
markersize = 5
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
            gbpses.append(float(line.strip().split(",")[3]) / 1000)

    return statistics.median(gbpses)


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern", help = "access pattern",
                        choices = ["fix", "random"], default = "fix")
    args = parser.parse_args()

    pdffile = "graph/graph_lat_{}.pdf".format(args.pattern)

    fig, ax = plt.subplots()

    dma_lens = [ 8, 16, 32, 64, 128, 256, 512, 1024, 2048 ]
    xticks = list(range(9))
    
    yaxis = []

    for dma_len in dma_lens:
        f = ("output/pciebench_lat_read_ptr-{}_len-{}.txt".format(args.pattern,
                                                                  dma_len))
        yaxis.append(parse(f))

    ax.plot(xticks, yaxis, marker = get_marker(), color = get_color())
    
    plt.xticks(xticks, dma_lens)
    #ax.set_xscale("log", basex = 2)
    plt.yticks(list(map(lambda x: x * 5, range(6))))

    ax.tick_params(labelsize = fontsize)
    ax.set_ylabel("latency (usec)", fontsize = fontsize)
    ax.set_xlabel("transfer size (byte)", fontsize = fontsize)
    
    ax.grid(True, linestyle = "--", linewidth = 0.5)

    change_aspect_ratio(ax, 2)

    print("save '{}'".format(pdffile))
    plt.savefig(pdffile, bbox_inches = "tight", pad_inches = 0.005)

if __name__ == "__main__":
    main()
