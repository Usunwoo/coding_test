s = input().upper()
alpha = list(set(s))

arr = []
for i in alpha:
    arr.append(s.count(i))
if arr.count(max(arr)) > 1:
    print("?")
else:
    print(alpha[arr.index(max(arr))])
