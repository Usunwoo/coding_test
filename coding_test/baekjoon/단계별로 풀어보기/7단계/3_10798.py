arr = [[""]*5 for i in range(15)]
for i in range(5):
    s = input()
    for j in range(len(s)):
        arr[j][i] = s[j]
for i in arr:
    print(*i, sep="", end="")
