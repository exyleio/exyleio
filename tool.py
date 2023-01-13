#!/usr/bin/env python3
from sys import argv

from util.actions import run, clone_all, print_help


if __name__ == "__main__":
    # argv[0] is "./tool.py" if called correctly

    # if no argument was passed
    if len(argv) == 1:
        print_help()
        exit()

    if argv[1] == "clone":
        clone_all()

    elif argv[1] == "run":
        if len(argv) < 3:
            print("Wat project tho?")
            print_help()
            exit()

        run(argv[2:])
