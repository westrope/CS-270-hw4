#!/usr/local/bin/python3
import sys

def main() :
    cols = sys.argv[1:]
    for i in range(0, len(cols)) : cols[i] = int(cols[i])-1

    for line in sys.stdin :
        line = line.split()
        lenline = len(line)
        for i in range(0, len(cols)) :
            c = cols[i]
            if c<lenline and c>=-lenline :
                print(line[c], end="")
            if i<len(cols)-1 : print(" ", end="")
        print("")

main()
