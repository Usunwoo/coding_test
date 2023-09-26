# https://www.acmicpc.net/problem/10430

import sys


A, B, C = map(int, sys.stdin.readline().rstrip().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)