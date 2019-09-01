#!/usr/bin/env python3

import argparse
import statistics


def parse_and_plot(dma_len, filename):
    
    rtts = []

    with open(filename, "r") as f:
        for line in f:
            rtts.append(float(line.strip().split(",")[3]) / 1000)

    #return statistics.median(rtts)
    print("{:<6} & {:<6} & {:<6} & {:<6} & {}".format(dma_len,
                                                  min(rtts),
                                                  statistics.median(rtts),
                                                  max(rtts),
                                                  statistics.pstdev(rtts)))


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern", help = "access pattern",
                        choices = ["fix", "random"], default = "fix")
    args = parser.parse_args()


    print("Len     Min     Med     Max     Stdev")
    for dma_len in [ 256, 512, 1024, 2048 ]:

        f = ("output/pciebench_lat2_" +
             "read_ptr-{}_len-{}.txt".format(args.pattern, dma_len))
                                             
        parse_and_plot(dma_len, f)

if __name__ == "__main__":
    main()
