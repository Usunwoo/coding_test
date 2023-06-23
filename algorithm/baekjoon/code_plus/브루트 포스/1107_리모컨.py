# https://www.acmicpc.net/problem/1107

import sys


n = int(sys.stdin.readline().rstrip()) # 이동해야 하는 채널
m = int(sys.stdin.readline().rstrip()) # 고장난 리모컨 숫자의 개수
broken_btn = list(map(int, sys.stdin.readline().rstrip().split(" "))) # 고장난 리모컨 숫자 리스트

now_channel = 100 # 현재 채널



"""sudo-code

"""