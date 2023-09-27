import sys

now_h, now_m = map(int, sys.stdin.readline().rstrip().split())
cook_m = int(sys.stdin.readline().rstrip())

cook_h, cook_m = cook_m // 60, cook_m % 60

if now_m + cook_m >= 60:
    if now_h + cook_h + 1 >= 24:
        print((now_h + cook_h + 1) - 24, (now_m + cook_m) -60)
    else:
        print((now_h + cook_h + 1), (now_m + cook_m) -60)
else:
    if now_h + cook_h >= 24:
        print((now_h + cook_h) - 24, (now_m + cook_m))
    else:
        print((now_h + cook_h), (now_m + cook_m))
