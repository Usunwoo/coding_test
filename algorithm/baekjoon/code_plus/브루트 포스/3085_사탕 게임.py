# https://www.acmicpc.net/problem/3085

import sys

n = int(sys.stdin.readline().rstrip())

arr = list()
for i in range(n): # 2차원 리스트로 만들기
    arr.append(list(sys.stdin.readline().rstrip()))

print(arr)

def check(): # 바뀐 리스트에서 가장 긴 줄이 어딘지 전부 계산해보기
    pass

for i in range(n): # 문자를 상하좌우로 바꿔보기
    for j in range(n):
        # 바꾸기
        check()
