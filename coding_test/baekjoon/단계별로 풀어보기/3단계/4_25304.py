import sys

total = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

num = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    num += a*b
    
if num == total:
    print("Yes")
else:
    print("No")
