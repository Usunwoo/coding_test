matrix = [list(map(int, input().split())) for _ in range(9)]
maximum = max([max(i) for i in matrix])
print(maximum)
[print(i+1, j+1) for i in range(9) for j in range(9) if matrix[i][j] == maximum]
