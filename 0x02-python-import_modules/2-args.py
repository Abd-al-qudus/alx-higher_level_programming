#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
	print("{}: {}".format(length, sys.argv[length]))
    else:
        print(f"{length} arguments")
        for i in range(1, length + 1):
            print(f"{i}: {sys.argv[i]}")
