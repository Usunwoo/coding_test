# https://www.acmicpc.net/problem/2309

import sys


arr = list()

# 9명의 키 받아오기
for _ in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))

arr = sorted(arr) # 리스트 오름차순 정렬
spy_height_sum = sum(arr) - 100 # 일곱 난쟁이가 아닌 두 명의 키의 합
first, second = 0, 0 # 난쟁이 두명의 키 초기화

for i in arr: # 첫 번째 난쟁이
    copy_arr = arr.copy()
    copy_arr.remove(i) # 첫 번째 난쟁이를 뺀 리스트(중복 방지)
    for j in copy_arr: # 두 번째 난쟁이
        if i+j == spy_height_sum: # 두 난쟁이의 키의 합이 spy_height_sum인지 확인
            # 맞으면 두 난쟁이의 키 저장
            first, second = i, j

# 리스트에서 두 난쟁이를 삭제 후 나머지를 출력
arr.remove(first)
arr.remove(second)
[print(i) for i in arr]

"""
9명의 키를 전부 더한 값에서 100을 빼면, 원래 있던 7명이 아닌 스파이 2명의 키의 합이 나옴.
9개의 값들 중 2개씩 뽑아 경우의 수를 전부 확인해 일곱 난쟁이가 아닌 두 명의 값을 찾음.
"""