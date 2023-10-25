n = int(input())
cnt = n

for i in range(n):
    s = input()
    arr = []
    last_alpha = ""
    for j in s:
        if j in arr:
            if last_alpha == j:
                pass
            else:
                cnt-=1
                break
        else:
            arr.append(j)
            last_alpha = j
            
print(cnt)
