# https://www.acmicpc.net/problem/1476

import sys


arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

arr2 = [1,1,1]
cnt = 1
while True:
    if arr == arr2:
        break
    if arr2[0] >= 15:
        arr2[0] = 1
    else:
        arr2[0]+=1
    if arr2[1] >= 28:
        arr2[1] = 1
    else:
        arr2[1]+=1
    if arr2[2] >= 19:
        arr2[2] = 1
    else:
        arr2[2]+=1
    cnt+=1
print(cnt)

# 범위
# (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
