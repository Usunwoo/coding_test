s = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0
for i in s:
    for j in dial:
        if i in j:
            time += dial.index(j)+2+1 # 숫자를 누르는데 걸리는 시간
print(time)
