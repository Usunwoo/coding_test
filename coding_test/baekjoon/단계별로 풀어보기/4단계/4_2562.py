import sys

arr = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
print(max(arr), arr.index(max(arr))+1, sep="\n")
