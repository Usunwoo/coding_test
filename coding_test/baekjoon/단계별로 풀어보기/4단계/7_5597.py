import sys

all = set([*range(1, 31)])
submit = set([int(input()) for _ in range(28)])

print(*sorted(all-submit), sep="\n")
