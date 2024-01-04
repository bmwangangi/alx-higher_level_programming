#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    plural = "s" if argc != 1 else ""
    period = "." if argc == 0 else ":"

    print("{} argument{}{}".format(argc, plural, period))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))

