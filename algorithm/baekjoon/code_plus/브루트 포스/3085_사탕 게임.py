# https://www.acmicpc.net/problem/3085

import sys
import copy
import time


n = int(sys.stdin.readline().rstrip())

arr = list()
for i in range(n): # 2차원 리스트로 만들기
    arr.append(list(sys.stdin.readline().rstrip()))

start = time.time()
def check(arr): # 바뀐 리스트에서 가장 긴 줄이 어딘지 전부 계산해보기
    longest = 0 # 전체 리스트중 가장 긴 길이 변수 선언
    cnt = 1
    for i in range(n): # 가로줄 확인
        text = ''
        for j in range(n):
            if arr[i][j] == text: # 전 문자랑 비교하면서 같으면 카운트 +1
                cnt+=1
            else: # 다르면 전체중 가장 긴 길이인지 확인 후 카운트 1로 초기화
                if longest<cnt:
                    longest = cnt
                cnt = 1
            text = arr[i][j] # 현재 텍스트 값 갱신
    for i in range(n): # 세로줄 확인
        text = ''
        for j in range(n):
            if arr[j][i] == text:
                cnt+=1
            else:
                if longest<cnt:
                    longest = cnt
                cnt = 1
            text = arr[j][i]

    return longest


longest_arr = list()

# 좌우 바꾸기
for i in range(n):
    for j in range(n-1):
        # 바꿀 값 구하기
        a = arr[i][j]
        b = arr[i][j+1]
        # 바꾸기
        arr1 = copy.deepcopy(arr)
        arr1[i][j] = b
        arr1[i][j+1] = a
        longest_arr.append(check(arr1)) # 가장 긴 줄 확인

# 상하 바꾸기
for i in range(n):
    for j in range(n-1):
        # 바꿀 값 구하기
        a = arr[j][i]
        b = arr[j+1][i]
        # 바꾸기
        arr1 = copy.deepcopy(arr)
        arr1[j][i] = b
        arr1[j+1][i] = a
        longest_arr.append(check(arr1)) # 가장 긴 줄 확인

print(max(longest_arr)) # 전체 중 가장 긴 값 최종 결과로 출력

end = time.time()
print(f"{end - start:.5f} sec")

# 00 01
# 01 02
# 10 11
# 11 12
# 20 21
# 21 22

# 00 10
# 10 20
# 01 11
# 11 21
# 02 12
# 12 22
