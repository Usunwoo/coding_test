n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for i in zip(a, b):
    arr = []
    for j in range(m):
        arr.append(i[0][j] + i[1][j])
    print(*arr)
