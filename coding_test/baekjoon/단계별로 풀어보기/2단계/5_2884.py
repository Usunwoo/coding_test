import sys

h, m = map(int, sys.stdin.readline().rstrip().split())

if m >= 45:
    print(h, m-45)
else:
    if h == 0:
        print(23, 60 + (m - 45))
    else:
        print(h-1, 60 + (m - 45))
