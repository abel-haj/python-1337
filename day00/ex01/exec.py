import sys

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        print(sys.argv[len(sys.argv)-i].swapcase()[::-1], end=" ")