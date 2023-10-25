original = [1, 1, 2, 2, 2, 8]
find = map(int, input().split())
for a, b in zip(original, find):
    print(a - b, end=" ")
