n = int(input())
arr = list(map(int, input().split()))

max_score = max(arr)
print(sum([i/max_score*100 for i in arr])/n)
