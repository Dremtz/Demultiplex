#!/usr/bin/env python
import argparse

def get_args():
    parser = argparse.ArgumentParser(description = "client input program")
    parser.add_argument("-i", "--inputfile", help = "index list", type=str, required = True)

    return parser.parse_args()

count_list = []

clinput = get_args()
i = clinput.inputfile

y = 0

with open (i, "r") as counts, open("outfile.tsv", "w") as o:
    for line in counts:
        l = line.split()
        count = l[-1]
        y = ((int(count)/363246735)*100)
        l.append(str(y))
        string = "\t".join(l)
        o.write(string)
        o.write("\n")
