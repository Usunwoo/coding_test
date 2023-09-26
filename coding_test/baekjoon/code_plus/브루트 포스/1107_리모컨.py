# https://www.acmicpc.net/problem/1107

import sys


n = int(sys.stdin.readline().rstrip()) # 이동해야 하는 채널
m = int(sys.stdin.readline().rstrip()) # 고장난 리모컨 숫자의 개수
broken_btn = sys.stdin.readline().rstrip().split(" ") # 고장난 리모컨 숫자 리스트

# 이동 가능한 가장 가까운 채널 찾기
min_cnt = abs(100 - n) # +, - 버튼만 사용한 경우(최대 경우의 수)
for i in range(1000001): # 가능한 전체 채널, 50000을 기준으로 내려오면서도 탐색해야 함으로 *
    channel = str(i)
    for j in range(len(channel)): # 채널의 각 자릿수 확인, 리모컨에 있는 숫자들로만 이루어진 경우 저장하고 아니면 패스
        if channel[j] in broken_btn:
            break
        if j == len(channel) - 1: # 각 자릿수가 전부 버튼에 있는 경우
            min_cnt = min(min_cnt, abs(n-i)+len(channel)) # 최소 버튼 입력 카운트 갱신
print(min_cnt)