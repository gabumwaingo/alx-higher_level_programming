#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n == 1:
        print("0 arguments.")
    else:
        if ((n - 1) == 1):
            print("1 argument:")
        else:
            print("{} arguments:".format(n - 1))
        for i in range(1, n):
            print("{0}: {1}".format(i, sys.argv[i]))
