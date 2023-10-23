t = int(input())
for _ in range(t):
    r, s = input().split()
    r = int(r)
    s = list(s)

    print(*[i*r for i in s], sep="")
