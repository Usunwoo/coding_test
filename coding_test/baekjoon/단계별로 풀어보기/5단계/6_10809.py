s = input()
for i in range(26):
    alpha = chr(i+97)
    if alpha in s:
        print(s.index(alpha), end=" ")
    else:
        print(-1, end=" ")
