#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print(f"{length} arguments.")
    elif length == 1:
        print(f"{length} argument:\n {length}: {sys.argv[length]}")
    else:
        print(f"{length} arguments")
        for i in range(1, length + 1):
            print(f"{i}: {sys.argv[i]}")
