#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 1:
        print(f"{count} argument:")
    elif count == 0:
        print(f"{count} arguments.")
    elif count > 1:
        print(f"{count} arguments:")
    for number in range(1, count + 1):
        print(f"{number}: {sys.argv[number]}")
