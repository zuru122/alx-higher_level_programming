#!/usr/bin/python3
# Author: Sunday, Justice Gabriel

if __name__ == "__main__":
    import sys

    # Exclude the script name from the argument count
    n = len(sys.argv) - 1

    if n == 0:
        print("{} arguments.".format(n))
    else:
        print("{} {}:".format(n, "argument" if n == 1 else "arguments"))

        for x in range(1, n + 1):
            print("{}: {}".format(x, sys.argv[x]))
