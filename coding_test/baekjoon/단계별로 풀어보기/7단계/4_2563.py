n = int(input())
arr = [[""]*100 for _ in range(100)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        arr[b+i][a:a+10] = ["X"]*10
cnt = 0
for i in arr:
    cnt += i.count("X")
print(cnt)
