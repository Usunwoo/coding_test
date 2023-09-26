import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())

print(a * int(str(b)[2]))
print(a * int(str(b)[1]))
print(a * int(str(b)[0]))
print(a * b)
