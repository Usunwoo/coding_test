import sys

n, m = map(int, input().split())
arr = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1] # python 언어의 swap 기능

print(*arr) # unpacking
