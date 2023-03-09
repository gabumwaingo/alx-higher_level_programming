#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n == 1:
        print(".")
    else:
        for i in range(1, n):
            print("{0}: {1}".format(i, sys.argv[i]))
