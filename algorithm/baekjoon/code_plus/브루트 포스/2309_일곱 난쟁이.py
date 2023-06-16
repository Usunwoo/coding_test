# https://www.acmicpc.net/problem/2309

import sys

arr = list()
for _ in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))

not_seven_height = sum(arr) - 100
arr = sorted(arr)

for i in arr:
    copy_arr = arr.copy()
    copy_arr.remove(i)
    print(copy_arr)
    for j in copy_arr:
        if i+j == not_seven_height:
            # print(arr.copy().remove([i, j]))
            pass


"""
9개의 값을 전부 더한 값에서 100을 빼면, 7개의 값이 아닌 2개의 값의 합이 나옴.
9개의 값들중 2개씩 뽑아 경우의 수를 전부 확인해 일곱 난쟁이가 아닌 두 명의 값을 찾음.
"""