#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addSum = 0
    length = len(sys.argv) - 1
    if length == 0:
        pass
    else:
        for i in range(1, length + 1):
            addSum += int(sys.argv[i])
    print(f"{addSum:d}")
