#!/usr/bin/env python3

import re
import sys
import os


def main():
    source = sys.argv[1]
    target = sys.argv[2]

    # find the last line of source
    lastLine = ""
    with open(target,'rb') as tgt:
        lineList = tgt.readlines()
        lastLine = lineList[-1]

    print("Start appending from : ", lastLine)
    with open(source,'rb') as src:
        with open(target,'a') as tgt:
            startAppend = False
            for line in src:
                if startAppend:
                    print(line)
                    tgt.write(line.decode('utf-8'))
                if line == lastLine:
                    startAppend = True


if __name__ == '__main__':
    main() 
