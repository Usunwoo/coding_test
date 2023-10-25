arr = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
s = input()

for i in arr:
    s = s.replace(i, "*")
print(len(s))
